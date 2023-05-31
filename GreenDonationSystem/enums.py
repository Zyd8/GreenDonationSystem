from enum import Enum

class Table(Enum):
    DONATION = "donation"
    TREES = "trees"

class DonColumn(Enum):
    ROWID = "rowid"
    MONEY = "money"

class TreColumn(Enum):
    ROWID = "rowid"
    MONEY = "money"
    SPECIES = "tree_species"
    SPECIES_QUANTITY = "tree_species_quantity"

class Order(Enum):
    ASCEND = "ASC"
    DESCEND = "DESC"
    ROWID = "rowid"