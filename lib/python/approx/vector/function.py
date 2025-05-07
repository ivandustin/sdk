from approx import Function as Base


class Function(Base):
    def __call__(self, x):
        return super().__call__(x.sum(axis=-2))
