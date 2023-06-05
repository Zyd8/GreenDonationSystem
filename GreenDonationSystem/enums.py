from enum import Enum

class Table(Enum):
    ACCOUNTS = "accounts"
    DONATIONS = "donations"
    TREES = "trees"
    
class AccColumn(Enum):
    ID = "donor_id"
    EMAIL = "email"
    PASSWORD = "password"

class DonColumn(Enum):
    ID = "donor_id"
    MONEY = "money"

class TreColumn(Enum):
    ID = "donor_id"
    MONEY = "money"
    SPECIES = "tree_species"
    SPECIES_QUANTITY = "tree_species_quantity"

class Order(Enum):
    ASCEND = "ASC"
    DESCEND = "DESC"
    ID = "donor_id"
    
class Signal(Enum):
    pass