Let's build a neural network using PyTorch to classify images. We'll use the CIFAR-10 dataset, which consists of 60,000 32x32 color images in 10 classes.

## Setting Up

First, let's import the necessary libraries and set up our device:

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
```

## Preparing the Data

Now, let's load and normalize the CIFAR-10 dataset:

```python
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4, shuffle=False, num_workers=2)

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
```

## Defining the Neural Network

Let's create a simple convolutional neural network:

```python
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = Net().to(device)
```

## Training the Network

Now, let's define the loss function and optimizer, and train the network:

```python
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

for epoch in range(2):  # loop over the dataset multiple times
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data[0].to(device), data[1].to(device)
        
        optimizer.zero_grad()
        
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
        if i % 2000 == 1999:    # print every 2000 mini-batches
            print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
            running_loss = 0.0

print('Finished Training')
```

## Testing the Network

Finally, let's test our network on the test dataset:

```python
correct = 0
total = 0
with torch.no_grad():
    for data in testloader:
        images, labels = data[0].to(device), data[1].to(device)
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy of the network on the 10000 test images: {100 * correct // total} %')
```

This neural network should achieve an accuracy of around 50-60% on the CIFAR-10 test set after just two epochs. With more epochs and a more complex architecture, you could achieve even higher accuracy.

Citations:
[1] https://pytorch.org/resources/
[2] https://www.geeksforgeeks.org/how-to-implement-neural-networks-in-pytorch/
[3] https://github.com/ritchieng/the-incredible-pytorch
[4] https://www.codecademy.com/learn/intro-to-py-torch-and-neural-networks
[5] https://pytorch.org/examples/
[6] https://pyimagesearch.com/2021/07/12/intro-to-pytorch-training-your-first-neural-network-using-pytorch/
[7] https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html
[8] https://www.youtube.com/watch?v=e5CDe00B3vE
[9] https://www.coursera.org/learn/deep-neural-networks-with-pytorch
[10] https://towardsdatascience.com/building-neural-network-using-pytorch-84f6e75f9a
[11] https://www.datacamp.com/tutorial/pytorch-tutorial-building-a-simple-neural-network-from-scratch
[12] https://www.learnpytorch.io/pytorch_extra_resources/
[13] https://www.appsilon.com/post/pytorch-neural-network-tutorial
[14] https://deeplearning.lipingyang.org/pytorch-resources/
[15] https://www.youtube.com/watch?v=mozBidd58VQ
[16] https://www.kaggle.com/general/242833
[17] https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html
[18] https://pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html
[19] https://www.machinelearningmastery.com/develop-your-first-neural-network-with-pytorch-step-by-step/
[20] https://pytorch.org/tutorials/beginner/pytorch_with_examples.html
[21] https://linuxblog.io/building-a-neural-network-with-pytorch/
[22] https://pytorch.org/tutorials/beginner/introyt/trainingyt.html
[23] https://github.com/mrdbourke/pytorch-deep-learning/
[24] https://www.youtube.com/watch?v=4p0G6tgNLis
[25] https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html
