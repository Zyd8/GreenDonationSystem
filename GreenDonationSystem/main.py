from accounts import Accounts
from enums import *

Accounts.init_db()
# account = Accounts(Accounts.rand_num_gen(), "meowa", "434")
# Accounts.insert_data(account)


print(Accounts.find_data(2587))

account = Accounts()
account.alter_data(2587, AccColumn.PASSWORD, "oh no")

print(Accounts.find_data(2587))

