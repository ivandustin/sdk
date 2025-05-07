from flax.nnx import Module, Rngs, Linear, sigmoid


class Fn(Module):
    def __init__(self, din, dout, width, rngs: Rngs):
        self.a = Linear(din, width, rngs=rngs)
        self.b = Linear(width, dout, rngs=rngs)

    def __call__(self, x):
        return self.b(sigmoid(self.a(x)))
