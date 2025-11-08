from flax.nnx import split, merge


def load(checkpointer, path, model):
    graph, _ = split(model)
    state = checkpointer.restore(path.resolve())
    return merge(graph, state)
