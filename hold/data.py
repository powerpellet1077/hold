from hold.log import Loggable
from hold.path import PathHandler
from json import loads, dumps
from typing import Any
class DataHandler(Loggable):
    def __init__(self):
        super().__init__()
        self._target_path = PathHandler().obtain_path()

    def get(self) -> Any:
        """returns currently saved configuration or data"""
        with open(self._target_path, "r") as f:
            try:
                return loads(f.read())
            except Exception as e:
                self.warning(f"error getting data from path {self._target_path}, err: {str(e)}")
                return {}

    def write(self, data) -> bool:
        """overwrites saved data, returns bool showing whether it was successful or not"""
        with open(self._target_path, "w") as f:
            try:
                f.write(dumps(data))
                return True
            except Exception as e:
                self.error(f"error writing data to path {self._target_path}, err: {str(e)}")
                return False