import sqlite3
from donation import Donation
from trees import Trees

conn = None
c = None

def enter():
    global conn, c
    conn = sqlite3.connect("GreenDonation.db")
    c = conn.cursor()

def exit():
    global conn
    conn.commit()
    conn.close()

def initialize_don():
    enter()
    c.execute("""CREATE TABLE IF NOT EXISTS donation (
                donation_id integer,
                money real
            )""")
    exit()

def initialize_trees():
    enter()
    c.execute("""CREATE TABLE IF NOT EXISTS trees (
                donation_id integer,
                money real,
                tree_species text,
                tree_species_quantity integer
            )""")
    exit()

def insert_data(table, don_id=None, money=0, tree_species="", tree_species_quantity=0):
    enter()
    if table == "donation":
        c.execute("INSERT INTO donation VALUES (?, ?)", (don_id, money))
    elif table == "trees":
        c.execute("INSERT INTO trees VALUES (?, ?, ?, ?)", (don_id, money, tree_species, tree_species_quantity))
    exit()

def read_table(table):
    enter()
    list = c.execute(f"SELECT * FROM {table}")
    for item in list:
        print(item)
    exit()

def insert_to_class(table):
    enter()
    donation_list = []
    c.execute(f"SELECT rowid, * FROM {table}")
    for item in c.fetchall():
        donation = Donation(None, 0)
        donation.donation_id = item[0]
        donation.money = item[1]
        donation_list.append(donation)
    exit()
    return donation_list
    
def find_row(table, rowid):
    enter()
    c.execute(f"SELECT rowid, * FROM {table} WHERE rowid = {rowid}")
    row = c.fetchone()
    if row:
        donation = Donation(row[0], row[1])
        print(donation)
    else:
        print("Row not found")
