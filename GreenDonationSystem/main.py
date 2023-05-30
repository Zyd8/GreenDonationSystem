import dbConnect
from donation import Donation
from trees import Trees

donation = dbConnect.insert_to_class("donation")

dbConnect.find_row("donation", 7)


