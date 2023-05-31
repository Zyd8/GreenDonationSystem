import dbConnect
from donation import Donation
from trees import Trees
from enums import *

dbConnect.initialize_trees()
dbConnect.initialize_don()

donation_list = dbConnect.insert_to_class(Table.DONATION)
trees_list = dbConnect.insert_to_class(Table.TREES)

dbConnect.alter_data(Table.TREES, 2, TreColumn.SPECIES, "Narra")

