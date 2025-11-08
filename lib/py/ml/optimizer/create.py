from flax.nnx import ModelAndOptimizer
from optax import adam


def create(model):
    return ModelAndOptimizer(model, adam(1e-3))
