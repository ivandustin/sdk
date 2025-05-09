from jax.numpy import sum
from uat.fn import Fn as Base


class Fn(Base):
    def __call__(self, x):
        return super().__call__(sum(x, axis=-2))
