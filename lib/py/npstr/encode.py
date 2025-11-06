from base64 import b64encode
from io import BytesIO
from numpy import ndarray, save


def encode(array: ndarray) -> str:
    buffer = BytesIO()
    save(buffer, array)
    return b64encode(buffer.getvalue()).decode("utf-8")
