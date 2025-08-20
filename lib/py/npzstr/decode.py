from base64 import b64decode
from io import BytesIO
from numpy import ndarray, load


def decode(batch: str) -> list[ndarray]:
    with load(BytesIO(b64decode(batch))) as result:
        return [result[key] for key in sorted(result.files)]
