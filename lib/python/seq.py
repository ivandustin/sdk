from flax.linen import Module, Embed, Dense, compact
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


class Decoder(Module):
    classes: int

    @compact
    def __call__(self, x):
        return Dense(self.classes)(x)


class Model(Module):
    classes: int
    dims: int
    neurons: int

    @compact
    def __call__(self, x):
        encode = Encoder(self.classes, self.dims)
        transformer = Transformer(self.neurons)
        decode = Decoder(self.classes)
        return decode(transformer(encode(x)))
