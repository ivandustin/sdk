from jax.numpy import sum
from approx import Function as Base


class Function(Base):
    def __call__(self, x):
        return super().__call__(sum(x, axis=-2))
