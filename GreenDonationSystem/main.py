from accounts import Accounts
from donations import Donations
from trees import Trees
from enums import *

Accounts.init_db()
Donations.init_db()
Trees.init_db()

# account = Accounts(Accounts.rand_num_gen(), "yow", "my password")
# Accounts.create_row(account)

# account = Accounts(Accounts.rand_num_gen(), "hmm", "sheesh")
# Accounts.create_row(account)

# account = Accounts(Accounts.rand_num_gen(), "meh", "addeeddd")
# Accounts.create_row(account)

# Accounts.read_table(AccColumn.ID, Order.ASCEND)

# donation = Donations()
# donation.extend_row(current_user=4431)
# donation.alter_row(4431, DonColumn.MONEY, 30)

# donation = Donations()
# donation.extend_row(current_user=8190)
# donation.alter_row(8190, DonColumn.MONEY, 39)

# trees = Trees()
# trees.extend_row(current_user=4578)
# trees.alter_row(4578, TreColumn.MONEY, 6)

Trees.get_total_money()