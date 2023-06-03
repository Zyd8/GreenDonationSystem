import sqlite3
import random
from donations import Donations
from trees import Trees
from accounts import Accounts
from enums import *

conn = None
c = None

def dbenter():
    global conn, c
    conn = sqlite3.connect("GreenDonation.db")
    c = conn.cursor()

def dbexit():
    global conn
    conn.commit()
    conn.close()

def initialize_accounts():
    dbenter()
    c.execute("""CREATE TABLE IF NOT EXISTS accounts (
                donor_id INTEGER PRIMARY KEY,
                email text,
                password text
            )""")
    dbexit()

def initialize_donations():
    dbenter()
    c.execute("""CREATE TABLE IF NOT EXISTS donations (
                donor_id INTEGER PRIMARY KEY,
                money real
            )""")
    dbexit()

def initialize_trees():
    dbenter()
    c.execute("""CREATE TABLE IF NOT EXISTS trees (
                donor_id INTEGER PRIMARY KEY,
                money real,
                tree_species text,
                tree_species_quantity integer
            )""")
    dbexit()


def read_table(table, base, order):
    dbenter()
    list = c.execute(f"SELECT * FROM {table.value} ORDER BY {base.value} {order.value}")
    for item in list:
        print(item)
    dbexit()

def del_table(table):
    dbenter()
    c.execute(f"DROP TABLE {table.value}")
    dbexit()
    

def insert_data(table, email="", password="", money=0, tree_species="", tree_species_quantity=0):
    id = rand_num_gen()
    dbenter()
    if table.value == Table.ACCOUNTS.value:
        object = Accounts(id) 
        object.email = email
        object.password = password
        c.execute(f"INSERT INTO {table.value} VALUES (?, ?, ?)", (id, object.email, object.password))
    elif table.value == Table.DONATIONS.value:
        object = Donations(id) 
        object.money = money
        c.execute(f"INSERT INTO {table.value} VALUES (?, ?)", (id, object.money))
    elif table.value == Table.TREES.value:
        object = Trees(id)
        object.money = money
        object.species = tree_species
        object.quantity = tree_species_quantity
        c.execute(f"INSERT INTO {table.value} VALUES (?, ?, ?, ?)", (id, object.money, object.species, object.species_quantity))
    dbexit()

def find_data(table, donor_id):
    dbenter()
    c.execute(f"SELECT * FROM {table.value} WHERE donor_id = {donor_id}")
    row = c.fetchone()
    if table.value == Table.ACCOUNTS.value:
        if row:
            accounts = Accounts(row[0], row[1], row[2])
            return accounts
        else:
            print(f"Row not found in {table.value}")
    elif table.value == Table.DONATIONS.value:       
        if row:
            donations = Donations(row[0], row[1])
            return donations
        else:
            print(f"Row not found in {table.value}")
    elif table.value == Table.TREES.value:
        if row:
            trees = Trees(row[0], row[1], row[2], row[3])
            return trees
        else:
            print(f"Row not found in {table.value}")
    dbexit()

def alter_data(table, donor_id, column, value):
    dbenter()
    c.execute(f"UPDATE {table.value} SET {column.value} = '{value}' WHERE donor_id = {donor_id}")
    dbexit()
    
def del_row(table, donor_id):
    dbenter()
    c.execute(f"DELETE FROM {table.value} WHERE donor_id = {donor_id}")
    dbexit()
    
def rand_num_gen():
    rand_num = random.randint(0, 9999)
    dbenter()
    while True:
        c.execute(f"SELECT * FROM {Table.ACCOUNTS.value} WHERE {AccColumn.ID.value} = ?", (rand_num,))
        result = c.fetchone()
        if result is None:
            break  
        rand_num = random.randint(0, 9999)
    dbexit()
    return rand_num
    
def verify(email, password):
    dbenter()
    c.execute(f"SELECT * FROM {Table.ACCOUNTS.value} WHERE {AccColumn.EMAIL.value} = ?", (email,))
    result = c.fetchone()
    if result:
        c.execute(f"SELECT * FROM {Table.ACCOUNTS.value} WHERE {AccColumn.PASSWORD.value} = ?", (password,))
        if c.fetchone():
            current_user = result[0] 
            dbexit()
            return "0", current_user
        else:
            dbexit()
            return "1", None
    else:
        dbexit()
        return "2", None
