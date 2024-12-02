# docker run --gpus all my-cuda-app nvidia-smi
# Set the base image to a CUDA-enabled Ubuntu image
FROM nvidia/cuda:12.4.1-base-ubuntu22.04

# Add metadata labels
LABEL maintainer="Your Name <your.email@example.com>"
LABEL version="1.0"
LABEL description="This Docker image is configured to run CUDA applications with NVIDIA GPU support."

# Check for GPU availability (Note: This check is more suitable to be run in the container, not during the build)
RUN [ -e /dev/nvidia0 ] && echo "GPU available" || echo "No GPU found"

# Update package lists and install CUDA command line tools
RUN apt-get update && apt-get install -y cuda-command-line-tools-12-4

# Add your application-specific instructions here
