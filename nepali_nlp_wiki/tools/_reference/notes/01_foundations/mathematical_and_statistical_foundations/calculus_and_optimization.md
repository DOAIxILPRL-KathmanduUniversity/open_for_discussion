# Calculus & Optimization: The Learning Process

> [!IMPORTANT] Gist
> If Linear Algebra is the engine, Calculus is the driver. Multivariate calculus allows us to calculate how tiny changes in model weights affect the error, while Optimization Theory provides the algorithms to navigate the "loss landscape" toward the global minimum (Ghayoumi, 2026).

## 1. Multivariate Calculus
Deep learning models are massive composite functions. To train them, we need to find the partial derivatives of the loss function with respect to every weight.
- **The Gradient ($\nabla$)**: A vector of partial derivatives. It points in the direction of steepest ascent.
- **The Chain Rule**: The backbone of **Backpropagation**. It allows us to compute derivatives of nested functions: $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$.
- **The Hessian Matrix**: A matrix of second-order partial derivatives. It captures the **curvature** of the loss function.
    - **Saddle Points**: Points where the gradient is zero but are not local minima. Common in high-dimensional optimization.

## 2. Optimization Theory
Optimization is the process of adjusting parameters $\theta$ to minimize a loss function $J(\theta)$.

### Gradient-Based Optimizers
- **Gradient Descent (GD)**: The simplest algorithm, moving in the direction of $-\nabla J(\theta)$.
- **Stochastic Gradient Descent (SGD)**: Updates weights using only one sample or a small batch, adding noise that helps escape local minima.
- **Momentum**: Accelerates SGD in the relevant direction and dampens oscillations by using a moving average of gradients.

### Adaptive Learning Rate Optimizers
- **RMSprop**: Adjusts the learning rate for each parameter by using a moving average of squared gradients. Prevents the learning rate from decaying too quickly.
- **Adam (Adaptive Moment Estimation)**: Combines momentum and RMSprop. It is the de facto standard for most NLP and Deep Learning tasks.

## 3. Convex vs. Non-Convex Optimization
- **Convex**: The loss landscape is a bowl; any local minimum is the global minimum. (e.g., Linear Regression).
- **Non-Convex**: The landscape has many hills, valleys, and saddle points. (e.g., Deep Neural Networks).

## 4. Regularization: Improving Generalization
Techniques to prevent overfitting by penalizing large weights:
- **L1 Regularization (Lasso)**: Adds $\lambda \sum |w_i|$ to the loss. Promotes sparsity (some weights become exactly zero).
- **L2 Regularization (Ridge)**: Adds $\lambda \sum w_i^2$ to the loss. Encourages smaller weights but rarely makes them zero.
- **Weight Decay**: The L2 regularization implementation in modern optimizers like AdamW.

---

#foundations #calculus #optimization #backpropagation #adam #regularization
