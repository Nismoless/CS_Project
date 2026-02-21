from interface import Interface
from irshashdict import IRSystemHashDict

def test_interface():
    inventory = IRSystemHashDict()
    inventory.load_data("spotify-2023-uid.csv")
    Interface.inventory_cl(inventory)
test_interface()