from base64 import b64decode, b64encode
from io import BytesIO
from numpy import load, save


def to_string(array):
    buffer = BytesIO()
    save(buffer, array)
    return b64encode(buffer.getvalue()).decode("utf-8")


def to_array(string):
    return load(BytesIO(b64decode(string)))
