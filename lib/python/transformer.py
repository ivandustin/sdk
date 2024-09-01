from flax.linen import Module, Dense, Sequential, compact
from selfattention import SelfAttention
from neurons import Neurons


class Transformer(Module):
    neurons: int

    @compact
    def __call__(self, x):
        dims = x.shape[-1]
        return Sequential(
            [
                SelfAttention(),
                Neurons(self.neurons),
                Dense(dims),
            ]
        )(x)
