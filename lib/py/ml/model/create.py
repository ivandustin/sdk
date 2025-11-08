from ml.paths.txt import DIMS, CLASSES, NEURONS, EMBEDS
from ml.txt.list.read import read as read_list
from ml.modules.model import Model
from ml.txt.read import read
from ml import rngs


def create():
    embeds = read_list(EMBEDS)
    classes = read(CLASSES)
    dims = read(DIMS)
    neurons = read(NEURONS)
    return Model(embeds, classes, dims, neurons, rngs=rngs)
