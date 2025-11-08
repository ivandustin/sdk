from .state.load import load as fn
from .model.create import create
from .paths.state import MODEL


def load(checkpointer):
    model = create()
    if MODEL.exists():
        model = fn(checkpointer, MODEL, create())
    return model
