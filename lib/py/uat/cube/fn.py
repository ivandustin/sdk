from jax.numpy import prod
from uat.mat.fn import Fn as Base


class Fn(Base):
    def __call__(self, x):
        return super().__call__(prod(x, axis=-3))
