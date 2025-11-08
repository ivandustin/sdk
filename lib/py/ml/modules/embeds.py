from flax.nnx import Rngs, Module, Embed, List
from jax.numpy import array


class Embeds(Module):
    def __init__(self, width: int, lengths: list[int], rngs: Rngs):
        self.embeds = List([Embed(n, width, rngs=rngs) for n in lengths])

    def __call__(self, xs):
        return array([self.embeds[i](x) for i, x in enumerate(xs)])
