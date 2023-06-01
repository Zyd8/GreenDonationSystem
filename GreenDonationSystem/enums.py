from enum import Enum

class Table(Enum):
    ACCOUNTS = "accounts"
    DONATIONS = "donations"
    TREES = "trees"
    
class AccColumn(Enum):
    ROWID = "rowid"
    EMAIL = "email"
    PASSWORD = "password"

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