from flax.nnx import split


def save(checkpointer, path, model):
    _, state = split(model)
    checkpointer.save(path.resolve(), state, force=True)
