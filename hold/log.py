from loguru._logger import Logger, Core
from sys import stdout, exit
class Loggable(Logger):
    """class that provides logging functionality for objects"""
    def __init__(self):
        super().__init__(
            core=Core(),
            exception=None,
            depth=0,
            record=False,
            lazy=False,
            colors=False,
            raw=False,
            capture=True,
            patchers=[],
            extra={}
        )

        self.level("INFO", color="<blue>")
        self.level("ERROR", color="<red>")
        self.level("WARNING", color="<yellow>")


        self.remove()
        self.add(self._sink, colorize=True, format="<level>[{level}] {message}</level>")

    def _sink(self, message):
        stdout.write(message.replace("__init__", "hold"))
        if "ERROR" in message: #the best of the best systems
            exit()