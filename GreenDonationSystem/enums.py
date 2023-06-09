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
    TOOLS = "tools"
    TOOLS_QUANTITY = "tools_quantity"
    PRODUCTS = "products"
    PRODUCTS_QUANTITY = "products_quantity"

class TreColumn(Enum):
    ID = "donor_id"
    MONEY = "money"
    TOOLS = "tools"
    TOOLS_QUANTITY = "tools_quantity"
    PRODUCTS = "products"
    PRODUCTS_QUANTITY = "products_quantity"
    # fix the enums FIRSTTT
    SPECIES = "tree_species"
    SPECIES_QUANTITY = "tree_species_quantity"
    
class OceColumn(Enum):
    ID = "donor_id"
    MONEY = "money"
    TOOLS = "tools"
    TOOLS_QUANTITY = "tools_quantity"
    PRODUCTS = "products"
    PRODUCTS_QUANTITY = "products_quantity"

class Donated(Enum):
    ID = "donor_id"
    MONEY = "money"
    TOOLS = "tools"
    TOOLS_QUANTITY = "tools_quantity"
    PRODUCTS = "products"
    PRODUCTS_QUANTITY = "products_quantity"
    SPECIES = "tree_species"
    SPECIES_QUANTITY = "tree_species_quantity"
    

class Order(Enum):
    ASCEND = "ASC"
    DESCEND = "DESC"
    ID = "donor_id"
    
class Signal(Enum):
    pass

# ONCE THERE IS A DONATION, IT WILL BE STORED IN ANOTHER TABLE CALLED DONATED 
# TABLE WHICH WILL STORE THE DONOR_ID TO A NON-PRIMARY KEY COLUMN. ONCE MOVED,
# THE ROW OF THE DONOR_ID WILL BE DELETED EITHER THE DONATIONS, TREES, OCEANS.