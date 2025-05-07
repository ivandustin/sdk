from jax.numpy import ones
from flax.nnx import Rngs
from approx.vector import Function


def test():
    function = Function(2, 3, 4, rngs=Rngs(0))
    yhat = function(ones((2, 2, 2)))
    assert yhat.shape == (2, 3)
