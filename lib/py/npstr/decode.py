from base64 import b64decode
from io import BytesIO
from numpy import ndarray, load


def decode(string: str) -> ndarray:
    return load(BytesIO(b64decode(string)))
