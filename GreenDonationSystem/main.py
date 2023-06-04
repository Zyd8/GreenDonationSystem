from accounts import Accounts
from donations import Donations
from trees import Trees
from enums import *

Accounts.init_db()
Donations.init_db()
Trees.init_db()

account = Accounts(Accounts.rand_num_gen(), "yow", "my password")
Accounts.create_row(account)

# account = Accounts()
# account.alter_row(5408, AccColumn.PASSWORD, "oh no n oon ono nn")

# donation = Donations()
# donation.alter_row(7641, DonColumn.MONEY, 1000000)

# print(Accounts.read_row(2587))

