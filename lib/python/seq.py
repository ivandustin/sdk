from flax.linen import Module, Embed, compact
from jax.numpy import arange
from transformer import Transformer


class Encoder(Module):
    classes: int
    dims: int

    @compact
    def __call__(self, x):
        length = x.shape[1]
        embedding = Embed(self.classes, self.dims)
        position = Embed(length, self.dims)
        return embedding(x) * position(arange(length))


class Model(Module):
    classes: int
    dims: int
    neurons: int

    @compact
    def __call__(self, x):
        encode = Encoder(self.classes, self.dims)
        transformer = Transformer(self.neurons, self.classes)
        return transformer(encode(x))
