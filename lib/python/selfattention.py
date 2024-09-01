from flax.linen import Module, Dense, compact


class SelfAttention(Module):
    @compact
    def __call__(self, x):
        dims = x.shape[-1]
        q = Dense(dims)(x)
        k = Dense(dims)(x)
        v = Dense(dims)(x)
        return q @ k.T @ v
