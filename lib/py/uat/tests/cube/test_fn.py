from jax.numpy import ones
from flax.nnx import Rngs
from uat.cube.fn import Fn


def test():
    f = Fn(5, 6, 7, rngs=Rngs(0))
    yhat = f(ones((2, 3, 4, 5)))
    assert yhat.shape == (2, 6)
