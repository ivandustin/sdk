from jax.numpy import ones
from flax.nnx import Rngs
from ml.modules.model import Model


def test():
    model = Model([1, 2, 3], 2, 3, 4, rngs=Rngs(0))
    assert model(ones((3, 4), dtype=int)).shape == (2,)
