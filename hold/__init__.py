from hold.data import DataHandler
from hold.log import Loggable


class Hold(Loggable):
    def __init__(self):
        super().__init__()
        self.d = DataHandler()

    def hold(self, key:str="global", dat="placeholder"):
        """stores/overwrites the data present at the given key"""
        try:
            d = self.d.get()
            d[key] = dat
            self.d.write(d)
        except Exception as e:
            self.error(f"unable to write new data to key {key}, err: {str(e)}")

    def retrieve(self, key:str="global"):
        try:
            dat = self.d.get()
            if key in dat:
                return self.d.get()[key]
            else:
                self.error(f"key {key} not found inside hold, halting")
        except Exception as e:
            self.error(f"unable to retrieve data from key {key}, err: {str(e)}")