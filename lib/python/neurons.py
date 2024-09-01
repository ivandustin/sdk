from flax.linen import Module, Dense, Sequential, compact, sigmoid


class Neurons(Module):
    neurons: int

    @compact
    def __call__(self, x):
        return Sequential([Dense(self.neurons), sigmoid])(x)
