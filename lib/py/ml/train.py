from optax.losses import softmax_cross_entropy_with_integer_labels
from flax.nnx import jit, value_and_grad, vmap


@jit
def train(optimizer, model, x, y):
    def loss(model):
        yhat = vmap(model)(x)
        return softmax_cross_entropy_with_integer_labels(yhat, y).mean()

    loss, grads = value_and_grad(loss)(model)
    optimizer.update(grads)
    return loss
