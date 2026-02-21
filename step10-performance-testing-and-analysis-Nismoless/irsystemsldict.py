from song import Song
import csv
from irsystemabs import IRSystemAbstract
from irslldict import IRSystemLL
from sldict import SLDict

class IRSystemSL(IRSystemLL):
    def __init__(self):
        self._dict_items = SLDict()