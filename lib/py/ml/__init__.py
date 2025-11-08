from flax.nnx import Rngs
from .seed.create import create

rngs = Rngs(create())
