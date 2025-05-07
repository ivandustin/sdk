from flax.nnx import Module, Rngs, Linear, sigmoid


class Fn(Module):
    def __init__(self, din, dout, n, rngs: Rngs):
        self.a = Linear(din, n, rngs=rngs)
        self.b = Linear(n, dout, rngs=rngs)

    def __call__(self, x):
        return self.b(sigmoid(self.a(x)))
