from jax.numpy import ones
from flax.nnx import Rngs
from uat.mat import Fn


def test():
    f = Fn(2, 3, 4, rngs=Rngs(0))
    yhat = f(ones((2, 2, 2)))
    assert yhat.shape == (2, 3)
