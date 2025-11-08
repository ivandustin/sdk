from pathlib import Path


def read(filepath: Path) -> list[int]:
    return list(map(int, filepath.read_text().split(" ")))
