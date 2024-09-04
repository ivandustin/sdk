from flax.linen import Module


class SelfAttention(Module):
    def __call__(self, x):
        return x @ x.T @ x
