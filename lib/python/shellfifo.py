from asyncio import Queue as AsyncQueue
from subprocess import Popen, PIPE
from threading import Thread
from shutil import which
from queue import Queue
from sys import stderr


def create(command: str) -> Queue:
    inputs: Queue = Queue()
    Thread(target=writer, args=(inputs, command), daemon=True).start()
    return inputs


def writer(inputs: Queue, command: str) -> None:
    with create_process(command) as process:
        channels: Queue = Queue()
        Thread(target=reader, args=(process, channels), daemon=True).start()
        while True:
            query, channel = inputs.get()
            process.stdin.write(query + "\n")
            process.stdin.flush()
            channels.put(channel)


def reader(process, channels: Queue) -> None:
    while True:
        channel: AsyncQueue = channels.get()
        channel.put_nowait(process.stdout.readline().strip())


def create_process(command: str):
    bash = which("bash")
    if bash is None:
        raise FileNotFoundError("No bash found")
    return Popen(
        [bash, "-c", command],
        stderr=stderr,
        stdout=PIPE,
        stdin=PIPE,
        text=True,
    )
