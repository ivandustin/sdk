from jax.numpy import ones
from flax.nnx import Rngs
from ml.modules.embeds import Embeds


def test():
    embeds = Embeds(2, [1, 2, 3], rngs=Rngs(0))
    assert embeds(ones((3, 4), dtype=int)).shape == (3, 4, 2)
