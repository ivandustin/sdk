from contextlib import contextmanager
from os import chdir, getcwd


@contextmanager
def pushd(dir):
    cwd = getcwd()
    chdir(dir)
    try:
        yield
    finally:
        chdir(cwd)
