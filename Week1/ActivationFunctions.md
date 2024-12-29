Understanding activation functions is crucial in neural networks, as they determine whether a neuron should "fire" based on its input. Here’s a concise overview of key activation functions and their characteristics:

## Activation Functions Overview

1. **Purpose**: Activation functions process the weighted sum of inputs plus a bias to decide if a neuron activates, mimicking biological neurons.

2. **Step Function**:
   - **Definition**: Outputs 1 if the input exceeds a threshold; otherwise, outputs 0.
   - **Drawback**: Binary output limits learning and complicates multi-class classification.

3. **Linear Function**:
   - **Definition**: Outputs are directly proportional to input (A = cx).
   - **Drawback**: Constant gradient leads to ineffective learning; multiple layers collapse into a single linear transformation.

4. **Sigmoid Function**:
   - **Definition**: Outputs values between 0 and 1, providing smooth gradients.
   - **Advantages**: Nonlinear, suitable for binary classification.
   - **Drawback**: Suffers from vanishing gradients at extremes, slowing learning.

5. **Tanh Function**:
   - **Definition**: Similar to sigmoid but outputs values between -1 and 1.
   - **Advantages**: Stronger gradients than sigmoid; retains nonlinearity.
   - **Drawback**: Also faces the vanishing gradient problem.

6. **ReLU (Rectified Linear Unit)**:
   - **Definition**: Outputs the input directly if positive; otherwise, outputs 0 (A(x) = max(0,x)).
   - **Advantages**: Nonlinear, promotes sparse activations (efficient computation).
   - **Drawbacks**: Can lead to "dying ReLU" where neurons become inactive due to zero gradients.

7. **Choosing Activation Functions**:
   - Use sigmoid for binary classification problems.
   - Start with ReLU for general purposes unless specific characteristics of the function suggest otherwise.

Research continues into developing better activation functions to enhance neural network performance.

Citations:
[1] https://medium.com/the-theory-of-everything/understanding-activation-functions-in-neural-networks-9491262884e0
