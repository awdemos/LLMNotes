
#!/bin/bash

# Adapted from https://stackoverflow.com/a/47436840

function lib_installed() { /sbin/ldconfig -N -v $(sed 's/:/ /' <<< $LD_LIBRARY_PATH) 2>/dev/null | grep $1; }
function check() { lib_installed $1 && echo "$1 is installed" || echo -e "\nERROR: $1 is NOT installed\n"; }
check libcuda.so
check libcudart
check libcudnn

if ! command -v nvcc &>/dev/null
then
    echo -e "\nnvcc is not installed\n"
else
    nvcc --version
fi

if ! command -v nvidia-smi &>/dev/null
then
    echo -e "\nnvidia-smi is not installed\n"
else
    nvidia-smi
fi

echo "Run tensorflow_mnist_test to test GPU funtion for training/testing on the MNIST dataset."
