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
                money real
            )""")
    exit()

def initialize_trees():
    enter()
    c.execute("""CREATE TABLE IF NOT EXISTS trees (
                money real,
                tree_species text,
                tree_species_quantity integer
            )""")
    exit()

def insert_to_class(table):
    enter()
    object_list = []
    c.execute(f"SELECT rowid, * FROM {table.value}")
    for item in c.fetchall():
        if table.value == "donation":
            object = Donation()
            object.donation_id = item[0]
            object.money = item[2]
            object_list.append(object)
        elif table.value == "trees":
            object = Trees()
            object.donation_id = item[0]
            object.money = item[1]
            object.species = item[2]
            object.quantity = item[3]
            object_list.append(object)
    exit()
    return object_list

def insert_data(table, money=0, tree_species="", tree_species_quantity=0):
    enter()
    if table.value == "donation":
        c.execute("INSERT INTO donation VALUES (?)", (money))
    elif table.value == "trees":
        c.execute("INSERT INTO trees VALUES (?, ?, ?)", (money, tree_species, tree_species_quantity))
    exit()

def read_table(table):
    enter()
    list = c.execute(f"SELECT * FROM {table.value}")
    for item in list:
        print(item)
    exit()

def find_data(table, rowid):
    enter()
    c.execute(f"SELECT rowid, * FROM {table.value} WHERE rowid = {rowid}")
    row = c.fetchone()
    if table.value == "donation":       
        if row:
            donation = Donation(row[0], row[1])
            return donation
        else:
            print(f"Row not found in {table.value}")
    elif table.value == "trees":
        if row:
            trees = Trees(row[0], row[1], row[2], row[3])
            return trees
        else:
            print(f"Row not found in {table.value}")
    exit()

def alter_data(table, rowid, column, value):
    enter()
    c.execute(f"UPDATE {table.value} SET {column.value} = '{value}' WHERE rowid = {rowid}")
    exit()