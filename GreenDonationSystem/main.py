import dbConnect
from enums import *

dbConnect.initialize_trees()
dbConnect.initialize_don()

donation_list = dbConnect.insert_to_class(Table.DONATION)
trees_list = dbConnect.insert_to_class(Table.TREES)

dbConnect.read_table(Table.TREES, TreColumn.ROWID, Order.DESCEND)

dbConnect.read_table(Table.TREES, TreColumn.ROWID, Order.ASCEND)