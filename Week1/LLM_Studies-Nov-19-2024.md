 ## Studying

(https://www.youtube.com/watch?v=iqmjzecbJHE)

- I like how he eludicates how to describe the equations in this video and in particular
the context of Q, K, V in self-attention.
- Q = Question the word wants to ask to all the neighboring words (asking vector, basically the probability if the meaning of a token is known)
- K = Every token word also has a K value which decides the probability of an answer being known.
- Q and K are multiplied to make a dot product. The dot product measures how similar the vectors are.
- if they are similar, The Key value is answering the Question value.
- V = Value vector ("has the question been answered? if yes take my value")
- So you do this with all the values in the text weighted by how well they are answering their questions which leads to a new token being generated.
- The newly generated token is enriched by the context of the neighboring tokens.
- QK^T is asking a question: every row of Q times every row of K and the reason why it is doing square root of d k, 
if every word is a standard distribution when they're doing dot product and they want to normalize back to the variance V which equals to 1.
- It is softmax because it is a weighted sum and the V matrix is the value.
- Multi-Head attention is multiple attempts to answer the questions in QKV.
- "Neural machine translation" by Bahdanau, Cho, Bengio (2014)
wrote the first example o fthe self-attention mechanism. (https://arxiv.org/pdf/1409.0473)
- "we introduce an extension to the encoder–decoder model which learns
to align and translate jointly. Each time the proposed model generates a word in a translation, it
(soft-)searches for a set of positions in a source sentence where the most relevant information is
concentrated. The model then predicts a target word based on the context vectors associated with
these source positions and all the previous generated target words."
- Recurrent Neural Network attention mechanism.
- In a neuro translation task, instead of directly inputting the appropriate tokens into the blocks to 
predict the next word they run it forward and backward and then they combine it together and run an additional neural network to let it decide
how much attention the current word (time T) should pay to the whole sequence and each word. Calculate all the weighted sum and then calculate a weighted sum together with the previous word.
- A lot of translation services used this at the time. 
- This solution is sequential and cannot be ran in parallel which is a big bottleneck.
- Transformer self-attention fixes this problem.
- The softmax is a useful optimization for computers (between sum up to be 1 to be positive)
- Encoder structure of the transformer is lineraly projected abd then Add and Norm layer
 which fixes the gradient descent bugs. Then it gets fed to a feed forward neural network.
- Add and Norm normalizes the data across the multiple dimensional space per token.
- 
- Masked during decoding hides the answers from the algo so as to prevent it from encoding the text again.

### Computational Complexity

Memory Complexity
| Model | Memory Complexity | Variables |
|-------|------------------|-----------|
| RNN | O(n·d) | n = sequence length |
| CNN | O(n·k·d) | d = model dimensionality |
| [Self-Attention] | O(n²·d) | k = kernel size (CNNs) |


Computational Complexity

| Model | Computational Complexity |
|-------|------------------------|
| RNN | O(n·d²) |
| CNN | O(n·k·d²) |
| [Self-Attention] | O(n²·d + n·d²) |

Self-Attention Complexity Breakdown:

O(n²·d): Computing query-key dot products
O(n·d²): Applying attention weights to values

## Key Points:
[Self-attention] has quadratic complexity with sequence length
Higher computational cost for long sequences vs [RNNs]/[CNNs]

Benefits:
- Better parallelization
- Superior capture of long-range dependencies

**This code generates a graph that models the memory complexity of self-attention as
O(n^2 log n)**

```python
import matplotlib.pyplot as plt
import numpy as np

# Data for the memory complexity cost graph
sequence_length = np.arange(1, 101)  # Sequence lengths from 1 to 100
memory_cost = sequence_length**2 * np.log(sequence_length)  # Complexity O(n^2 * log(n))

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(sequence_length, memory_cost, label='Memory Complexity O(n^2 log(n))', color='b')
plt.title('Memory Complexity Cost of Self-Attention')
plt.xlabel('Sequence Length n')
plt.ylabel('Memory Complexity')
plt.grid(True)
plt.legend()
plt.show()
```
# Add and Norm Layer in Transformer Architecture

The Add and Norm layer in the Transformer architecture solves several important problems:

### Mitigating the Vanishing Gradient Problem
- The "Add" part of the layer implements a residual connection, which allows gradients to flow more easily through the network during backpropagation.
- This helps combat the vanishing gradient problem that can occur in deep neural networks, especially those with many layers like the Transformer.

### Preserving Information
- The residual connection adds the input of the sublayer to its output, allowing the network to retain important information from earlier layers.
- This is particularly useful for maintaining the integrity of the original input as it passes through multiple layers of the network.

### Stabilizing Training
- The "Norm" part, which applies layer normalization, helps stabilize the training process by normalizing the activations of each layer.
- This normalization ensures that the input to each layer has a consistent scale and distribution, leading to faster convergence and improved performance.

### Enhancing Feature Representation
- By normalizing the activations, layer normalization helps create more expressive feature representations.
- It allows the network to focus on the relative importance of features rather than their absolute scales.

### Regularization Effect
- The normalization process introduces a slight noise to the data, which can act as a form of regularization.
- This potentially improves the model's generalization capabilities.

### Facilitating Deeper Architectures
- The combination of residual connections and normalization allows for the construction of much deeper networks without degradation in performance.
- This is crucial for the Transformer architecture, which often benefits from increased depth.

### Improving Gradient Flow
- The residual connection provides a direct path for gradients to flow backward through the network.
- This can help in training very deep networks more effectively.

### Maintaining Consistent Input Distribution
- Layer normalization helps maintain a similar input distribution across all hidden units in the neural network.
- This contributes to more stable and efficient training.

### Conclusion
By addressing these issues, the Add and Norm layer plays a crucial role in enabling the Transformer architecture to achieve high performance on various natural language processing tasks. It allows the model to be deeper, train more stably, and learn more effectively from the input data.


