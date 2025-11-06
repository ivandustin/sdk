from base64 import b64encode
from io import BytesIO
from numpy import savez


def encode(*args) -> str:
    buffer = BytesIO()
    savez(buffer, *args)
    return b64encode(buffer.getvalue()).decode("utf-8")
