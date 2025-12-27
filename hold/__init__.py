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
        """returns a saved value present at the given key"""
        try:
            dat = self.d.get()
            if key in dat:
                return self.d.get()[key]
            else:
                self.error(f"key {key} not found inside hold, halting")
        except Exception as e:
            self.error(f"unable to retrieve data from key {key}, err: {str(e)}")

    def list(self) -> str:
        """returns all saved values in a formatted string"""
        try:
            dat:dict = self.d.get()
            formatted = ""
            for elm in dat.keys():
                formatted += f"{elm} = {dat[elm]}\n"
            return formatted
        except Exception as e:
            self.error(f"unable to retrieve data, err: {str(e)}")
            return ""

    def clear(self, key:str="global"):
        """clears a saved value present at the given key"""
        try:
            dat = self.d.get()
            if key in dat:
                del dat[key]
            else:
                self.error(f"element {key} not in hold")
            self.d.write(dat)
        except Exception as e:
            self.error(f"unable to write new data to key {key}, err: {str(e)}")