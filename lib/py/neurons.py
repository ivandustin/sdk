from flax.linen import Module, Dense, compact, sigmoid


class Neurons(Module):
    neurons: int

    @compact
    def __call__(self, x):
        linear = Dense(self.neurons)
        return sigmoid(linear(x))
