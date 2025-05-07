from flax.linen import Module, Dense, compact
from neurons import Neurons


class Function(Module):
    neurons: int
    dims: int

    @compact
    def __call__(self, x):
        linear = Dense(self.dims)
        nonlinear = Neurons(self.neurons)
        return linear(nonlinear(x))
