import dbConnect as db
from enums import *

db.initialize_accounts()
db.initialize_trees()
db.initialize_donations()

accounts_list = db.insert_to_class(Table.ACCOUNTS)
donation_list = db.insert_to_class(Table.DONATIONS)
trees_list = db.insert_to_class(Table.TREES)

db.insert_data(Table.ACCOUNTS, email="a.com", password="76")
db.insert_data(Table.DONATIONS, money=10)
db.insert_data(Table.TREES, money=5, tree_species="oak")

accounts_list = db.insert_to_class(Table.ACCOUNTS)
donation_list = db.insert_to_class(Table.DONATIONS)
trees_list = db.insert_to_class(Table.TREES)

print(accounts_list)
print(trees_list)
print(donation_list)

