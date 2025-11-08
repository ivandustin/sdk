from pathlib import Path


def read(filepath: Path) -> int:
    return int(filepath.read_text())
