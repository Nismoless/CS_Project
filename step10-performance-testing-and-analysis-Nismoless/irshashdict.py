from song import Song
import csv
from irsystemabs import IRSystemAbstract
from irslldict import IRSystemLL
from hashdict import HashDict

class IRSystemHashDict(IRSystemLL):
    def __init__(self):
        self._dict_items = HashDict()