import numpy as np
import matplotlib.pyplot as plt

# Binary Step Activation Function
def binary_step(x):
    return np.heaviside(x, 1)

# Linear Activation Function
def linear(x):
    return x

# Sigmoid Activation Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Tanh Activation Function
def tanh(x):
    return np.tanh(x)

# ReLU Activation Function
def relu(x):
    return np.maximum(0, x)

# Softmax Activation Function
def softmax(x):
    exp_x = np.exp(x - np.max(x))  # for numerical stability
    return exp_x / exp_x.sum(axis=0)

# Example usage and plotting
x = np.linspace(-10, 10, 100)

plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.plot(x, binary_step(x))
plt.title('Binary Step Function')

plt.subplot(3, 2, 2)
plt.plot(x, linear(x))
plt.title('Linear Function')

plt.subplot(3, 2, 3)
plt.plot(x, sigmoid(x))
plt.title('Sigmoid Function')

plt.subplot(3, 2, 4)
plt.plot(x, tanh(x))
plt.title('Tanh Function')

plt.subplot(3, 2, 5)
plt.plot(x, relu(x))
plt.title('ReLU Function')

# Softmax typically applied to a vector; here we show its effect on a range
softmax_values = softmax(np.array([x]))
plt.subplot(3, 2, 6)
plt.plot(x, softmax_values.T)  # Transpose for correct shape
plt.title('Softmax Function')

plt.tight_layout()
plt.show()

