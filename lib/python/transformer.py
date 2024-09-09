from flax.linen import Module, compact
from jax import vmap
from selfattention import SelfAttention
from uat import Function


class Transformer(Module):
    neurons: int
    dims: int

    @compact
    def __call__(self, x):
        attention = vmap(SelfAttention())
        function = Function(self.neurons, self.dims)
        return function(attention(x))
