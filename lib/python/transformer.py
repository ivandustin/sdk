from flax.linen import Module, compact
from jax import vmap
from selfattention import SelfAttention
from uat import Function


class Transformer(Module):
    neurons: int

    @compact
    def __call__(self, x):
        dims = x.shape[-1]
        attention = vmap(SelfAttention())
        function = Function(self.neurons, dims)
        return function(attention(x))
