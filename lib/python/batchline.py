from dataclasses import dataclass
from functools import partial
from threading import Thread
from queue import Queue
from time import sleep
from os import environ


@dataclass
class Container:
    batch: list


def get(file):
    batch_size = int(environ.get("BATCH_LINE_SIZE", "128"))
    timeout = float(environ.get("BATCH_LINE_TIMEOUT", "0.01"))
    container = Container(batch=[])
    queue = Queue()
    thread = spawn(partial(read, file, container, batch_size, queue))
    spawn(partial(tick, thread, timeout, container, queue))
    while True:
        batch = queue.get()
        if batch is None:
            break
        yield batch
    if container.batch:
        yield container.batch


def read(file, container, batch_size, queue):
    for line in file:
        container.batch.append(line)
        if len(container.batch) == batch_size:
            queue.put(container.batch)
            container.batch = []
    queue.put(None)


def tick(thread, timeout, container, queue):
    while thread.is_alive():
        batch = container.batch
        sleep(timeout)
        if batch:
            if container.batch is batch:
                if len(container.batch) is len(batch):
                    queue.put(batch)
                    container.batch = []


def spawn(function):
    thread = Thread(target=function, daemon=True)
    thread.start()
    return thread
