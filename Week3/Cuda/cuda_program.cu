    #include <cuda_runtime.h>
    #include <iostream>

    __global__ void add(int *a, int *b, int *c, int N) {
        int idx = threadIdx.x + blockIdx.x * blockDim.x;
        if (idx < N) {
            c[idx] = a[idx] + b[idx];
        }
    }

    int main() {
        int N = 1000;
        int size = N * sizeof(int);
        int *a, *b, *c;
        int *d_a, *d_b, *d_c;

        // Allocate host memory
        a = (int*)malloc(size);
        b = (int*)malloc(size);
        c = (int*)malloc(size);

        // Initialize host arrays
        for (int i = 0; i < N; i++) {
            a[i] = i;
            b[i] = i;
        }

        // Allocate device memory
        cudaMalloc((void**)&d_a, size);
        cudaMalloc((void**)&d_b, size);
        cudaMalloc((void**)&d_c, size);

        // Copy data from host to device
        cudaMemcpy(d_a, a, size, cudaMemcpyHostToDevice);
        cudaMemcpy(d_b, b, size, cudaMemcpyHostToDevice);

        // Launch kernel
        add<<<(N + 255) / 256, 256>>>(d_a, d_b, d_c, N);

        // Copy result from device to host
        cudaMemcpy(c, d_c, size, cudaMemcpyDeviceToHost);

        // Print result
        for (int i = 0; i < 10; i++) {
            std::cout << c[i] << " ";
        }
        std::cout << std::endl;

        // Free memory
        free(a);
        free(b);
        free(c);
        cudaFree(d_a);
        cudaFree(d_b);
        cudaFree(d_c);

        return 0;
    }
