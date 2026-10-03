# intro to deep learning practice

# deep learning = subset of ml using neural networks
# "deep" means multiple layers

# biological neuron vs artificial neuron:
# dendrites -> inputs
# synapse -> weights
# cell body -> weighted sum + bias
# axon -> activation function
# output signal -> output

# activation functions:
# sigmoid -> output [0,1], good for probability
# relu -> max(0,x), most commonly used
# tanh -> output [-1,1]

# neural network: input layer -> hidden layer(s) -> output layer

# training:
# 1. forward propagation (compute output)
# 2. calculate loss (how wrong)
# 3. backward propagation (compute gradients)
# 4. update weights (gradient descent)

import numpy as np
import matplotlib.pyplot as plt


# activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return (x > 0).astype(float)

def tanh(x):
    return np.tanh(x)


# visualizing activation functions
x = np.linspace(-5, 5, 100)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

axes[0].plot(x, sigmoid(x), color="#e74c3c", linewidth=2)
axes[0].set_title("sigmoid")
axes[0].axhline(y=0, color='black', linewidth=0.5)
axes[0].axvline(x=0, color='black', linewidth=0.5)
axes[0].grid(True, alpha=0.3)
axes[0].set_ylim(-0.2, 1.2)

axes[1].plot(x, relu(x), color="#3498db", linewidth=2)
axes[1].set_title("relu")
axes[1].axhline(y=0, color='black', linewidth=0.5)
axes[1].axvline(x=0, color='black', linewidth=0.5)
axes[1].grid(True, alpha=0.3)

axes[2].plot(x, tanh(x), color="#2ecc71", linewidth=2)
axes[2].set_title("tanh")
axes[2].axhline(y=0, color='black', linewidth=0.5)
axes[2].axvline(x=0, color='black', linewidth=0.5)
axes[2].grid(True, alpha=0.3)
axes[2].set_ylim(-1.2, 1.2)

plt.suptitle("activation functions", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.show()


# perceptron - learning AND gate
print("perceptron - and gate\n")

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.random.randn(input_size) * 0.5
        self.bias = 0.0
        self.lr = learning_rate

    def predict(self, x):
        z = np.dot(x, self.weights) + self.bias
        return 1 if z >= 0.5 else 0

    def train(self, X, y, epochs=20):
        for epoch in range(epochs):
            errors = 0
            for xi, yi in zip(X, y):
                prediction = self.predict(xi)
                error = yi - prediction
                if error != 0:
                    errors += 1
                    self.weights += self.lr * error * xi
                    self.bias += self.lr * error
            if (epoch + 1) % 5 == 0 or errors == 0:
                print(f"  epoch {epoch + 1}: errors = {errors}")
            if errors == 0:
                break

X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])

perceptron = Perceptron(input_size=2, learning_rate=0.1)
print("training:")
perceptron.train(X_and, y_and, epochs=50)

print(f"\nweights: {perceptron.weights}")
print(f"bias: {perceptron.bias}")

print("\npredictions:")
for xi, yi in zip(X_and, y_and):
    pred = perceptron.predict(xi)
    print(f"  {xi} -> predicted: {pred}, actual: {yi}")


# neural network for XOR (needs hidden layer because xor is not linearly separable)
print("\n\nneural network - xor problem")
print("xor cant be solved by single perceptron, needs hidden layer\n")

class SimpleNeuralNetwork:
    def __init__(self):
        np.random.seed(42)
        # 2 inputs -> 2 hidden -> 1 output
        self.w1 = np.random.randn(2, 2) * 0.5
        self.b1 = np.zeros((1, 2))
        self.w2 = np.random.randn(2, 1) * 0.5
        self.b2 = np.zeros((1, 1))

    def forward(self, X):
        self.z1 = X @ self.w1 + self.b1
        self.a1 = sigmoid(self.z1)
        self.z2 = self.a1 @ self.w2 + self.b2
        self.a2 = sigmoid(self.z2)
        return self.a2

    def backward(self, X, y, output, lr=0.5):
        m = X.shape[0]

        # output layer
        dz2 = (output - y) * sigmoid_derivative(self.z2)
        dw2 = self.a1.T @ dz2 / m
        db2 = np.sum(dz2, axis=0, keepdims=True) / m

        # hidden layer
        dz1 = (dz2 @ self.w2.T) * sigmoid_derivative(self.z1)
        dw1 = X.T @ dz1 / m
        db1 = np.sum(dz1, axis=0, keepdims=True) / m

        # update
        self.w1 -= lr * dw1
        self.b1 -= lr * db1
        self.w2 -= lr * dw2
        self.b2 -= lr * db2

    def train(self, X, y, epochs=10000, lr=2.0):
        losses = []
        for epoch in range(epochs):
            output = self.forward(X)
            loss = np.mean((y - output) ** 2)
            losses.append(loss)
            self.backward(X, y, output, lr)

            if (epoch + 1) % 2000 == 0:
                print(f"  epoch {epoch + 1}: loss = {loss:.6f}")
        return losses

X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor = np.array([[0], [1], [1], [0]])

nn = SimpleNeuralNetwork()
print("training:")
losses = nn.train(X_xor, y_xor, epochs=10000, lr=2.0)

print(f"\npredictions:")
predictions = nn.forward(X_xor)
for xi, yi, pred in zip(X_xor, y_xor, predictions):
    rounded = round(pred[0])
    print(f"  {xi} -> predicted: {pred[0]:.4f} (={rounded}), actual: {yi[0]}")

# loss plot
plt.figure(figsize=(8, 5))
plt.plot(losses, color="#e74c3c", linewidth=1.5)
plt.title("xor neural network - training loss")
plt.xlabel("epoch")
plt.ylabel("mean squared error")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# gradient descent visualization
print("\ngradient descent demo")

# function: f(x) = x^2 + 2x + 1
def f(x):
    return x ** 2 + 2 * x + 1

def f_derivative(x):
    return 2 * x + 2

x_start = 4.0
lr = 0.1
x_history = [x_start]

for _ in range(20):
    gradient = f_derivative(x_history[-1])
    x_new = x_history[-1] - lr * gradient
    x_history.append(x_new)

print(f"starting point: x = {x_start}")
print(f"learning rate: {lr}")
print(f"minimum found at x = {x_history[-1]:.6f}")
print(f"f(x_min) = {f(x_history[-1]):.6f}")

x_plot = np.linspace(-5, 5, 100)
plt.figure(figsize=(8, 5))
plt.plot(x_plot, f(x_plot), color="#3498db", linewidth=2, label="f(x) = x^2 + 2x + 1")
plt.scatter(x_history, [f(x) for x in x_history], color="#e74c3c", s=60, zorder=5)
plt.plot(x_history, [f(x) for x in x_history], color="#e74c3c", linewidth=1,
         alpha=0.5, linestyle="--", label="gradient descent path")
plt.scatter(x_history[-1], f(x_history[-1]), color="#2ecc71", s=150,
            marker="*", zorder=6, label=f"minimum (x={x_history[-1]:.2f})")
plt.title("gradient descent optimization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
