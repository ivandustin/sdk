from flax.linen import Module


class SelfAttention(Module):
    def __call__(self, x):
        return x.sum(axis=0)
