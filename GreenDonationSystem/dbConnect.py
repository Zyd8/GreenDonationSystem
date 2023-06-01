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

def insert_to_class(table):
    id = rand_num_gen()
    dbenter()
    object_list = []
    c.execute(f"SELECT * FROM {table.value}")
    for item in c.fetchall():
        if table.value == Table.ACCOUNTS.value:
            object = Accounts(id, item[1], item[2])
            object_list.append(object)
        elif table.value == Table.DONATIONS.value:
            object = Donations(id, item[1])
            object_list.append(object)
        elif table.value == Table.TREES.value:
            object = Trees(id, item[1], item[2], item[3])
            object_list.append(object)
    dbexit()
    return object_list

def read_table(table, base, order):
    dbenter()
    list = c.execute(f"SELECT * FROM {table.value} ORDER BY {base.value} {order.value}")
    for item in list:
        print(item)
    dbexit()
    insert_to_class(table)

def del_table(table):
    dbenter()
    c.execute(f"DROP TABLE {table.value}")
    dbexit()
    insert_to_class(table)

def insert_data(table, donor_id=None, email="", password="", money=0, tree_species="", tree_species_quantity=0):
    dbenter()
    if table.value == Table.ACCOUNTS.value:
        c.execute(f"INSERT INTO {table.value} VALUES (?, ?, ?)", (donor_id, email, password))
    elif table.value == Table.DONATIONS.value:
        c.execute(f"INSERT INTO {table.value} VALUES (?, ?)", (donor_id, money))
    elif table.value == Table.TREES.value:
        c.execute(f"INSERT INTO {table.value} VALUES (?, ?, ?, ?)", (donor_id, money, tree_species, tree_species_quantity))
    dbexit()
    insert_to_class(table)

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
    insert_to_class(table)

def alter_data(table, donor_id, column, value):
    dbenter()
    c.execute(f"UPDATE {table.value} SET {column.value} = '{value}' WHERE donor_id = {donor_id}")
    dbexit()
    insert_to_class(table)
    
def del_data(table, donor_id):
    dbenter()
    c.execute(f"DELETE FROM {table.value} WHERE donor_id = {donor_id}")
    dbexit()
    insert_to_class(table)
    
def rand_num_gen():
    rand_num = random.randint(0, 9999)
    dbenter()
    while True:
        c.execute(f"SELECT donor_id FROM accounts WHERE donor_id = ?", (rand_num,))
        result = c.fetchone()
        if result is None:
            break  
        rand_num = random.randint(0, 9999)
    dbexit()
    return rand_num
    
    
    
# // When called, it provides a random number for the unique ID of databases
#     public int randNumGen(String dbName, String dbId) {
#         Random random = new Random();
#         int randNum = random.nextInt(9999);
#          try {
#             stmt = con.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE,
#                     ResultSet.CONCUR_UPDATABLE);
#             rs = stmt.executeQuery("SELECT " + dbId.toUpperCase() + " FROM " + dbName.toUpperCase() + " WHERE " + dbId.toUpperCase() + "="+randNum);
#             while (rs.next()) {
#                 randNum = random.nextInt(9999);
#                 rs = stmt.executeQuery("SELECT " + dbId.toUpperCase() + " FROM " + dbName.toUpperCase() + " WHERE " + dbId.toUpperCase() + "="+ randNum);
#             }
#             refreshRsStmt("accounts");
#         } 
#         catch (SQLException err) 
#         {
#             System.out.println(err.getMessage());
#         }
#         return randNum;
#     }