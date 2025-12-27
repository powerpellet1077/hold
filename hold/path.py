from hold.log import Loggable
from pathlib import Path
from platform import system
from os import getenv
from json import dumps

class PathHandler(Loggable):
    """used for getting a path to the configuration/data file"""
    def __init__(self, create_if_does_not_exist:bool=True):
        super().__init__()
        self.TARGET_CONF = "hold.json"

        if create_if_does_not_exist:
            self.create_if_does_not_exist()

    def obtain_path(self) -> Path|None:
        """returns a Path object with the target path if operating system is Windows or Linux, otherwise returns none."""
        sys = system()
        if sys == "Windows":
            return Path(getenv("APPDATA"))/self.TARGET_CONF
        elif sys == "Linux":
            return Path.home()/".config"/self.TARGET_CONF
        else:
            self.error(f"operating system {sys} not supported. no path returned")
            return None

    def create_if_does_not_exist(self) -> bool:
        """creates an empty data file if it does not exist already. returns true if it created a new file"""
        p = self.obtain_path()
        if not p.is_file():
            with open(p, "w") as f:
                f.write(dumps({}))
                return True
        return False