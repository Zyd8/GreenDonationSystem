from enum import Enum

class Table(Enum):
    DONATION = "donation"
    TREES = "trees"

class DonColumn(Enum):
    MONEY = "money"

class TreColumn(Enum):
    MONEY = "money"
    SPECIES = "tree_species"
    SPECIES_QUANTITY = "tree_species_quantity"
