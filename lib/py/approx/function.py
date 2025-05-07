from flax.nnx import Module, Rngs, Linear, sigmoid


class Function(Module):
    def __init__(self, inputs, outputs, neurons, rngs: Rngs):
        self.a = Linear(inputs, neurons, rngs=rngs)
        self.b = Linear(neurons, outputs, rngs=rngs)

    def __call__(self, x):
        return self.b(sigmoid(self.a(x)))
