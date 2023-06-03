import sqlite3
import random
from enums import *

class Accounts:
    
    @staticmethod
    def init_db():
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS accounts (
                        donor_id INTEGER PRIMARY KEY,
                        email text,
                        password text
                    )""")
        
    @staticmethod
    def rand_num_gen():
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            rand_num = random.randint(0, 9999)
            while True:
                c.execute(f"SELECT * FROM {Table.ACCOUNTS.value} WHERE {AccColumn.ID.value} = ?", (rand_num,))
                result = c.fetchone()
                if result is None:
                    break  
                rand_num = random.randint(0, 9999)
            return rand_num
    
    @staticmethod
    def verify_account(email, password):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute(f"SELECT * FROM {Table.ACCOUNTS.value} WHERE {AccColumn.EMAIL.value} = ?", (email,))
            result = c.fetchone()
            if result:
                c.execute(f"SELECT * FROM {Table.ACCOUNTS.value} WHERE {AccColumn.PASSWORD.value} = ?", (password,))
                if c.fetchone():
                    current_user = result[0] 
                    return "0", current_user
                else:
                    return "1", None
            else:

                return "2", None
        
    @staticmethod
    def read_row(donor_id):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute(f"SELECT * FROM {Table.ACCOUNTS.value} WHERE donor_id = ?", (donor_id,))
            row = c.fetchone()
            if row:
                accounts = Accounts(row[0], row[1], row[2])
                return accounts
            print("Record not found")
            
    
    @staticmethod
    def del_row(donor_id):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute(f"DELETE FROM {Table.ACCOUNTS.value} WHERE donor_id = {donor_id}")
        
    
    @staticmethod
    def read_table(base, order):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            list = c.execute(f"SELECT * FROM {Table.ACCOUNTS.value} ORDER BY {base.value} {order.value}")
            for item in list:
                print(item)
        
    @staticmethod
    def del_table():
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute(f"DROP TABLE {Table.ACCOUNTS.value}")
        
        
    def __init__(self, donor_id=None, email="", password=""):
        self.__donor_id = donor_id
        self.__email = email
        self.__password = password
        
    def __repr__(self):
        return f"Accounts(donor_id={self.donor_id}, email={self.email}, password={self.password})"
    
    @property
    def donor_id(self):
        return self.__donor_id
    
    @donor_id.setter
    def donor_id(self, value): 
        self.__donor_id = value
    
    @property
    def email(self):
        return self.__email
    
    @email.setter 
    def email(self, value):
        self.__email = value        
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        self.__password = value  
    
    def create_eow(self):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute(f"INSERT INTO {Table.ACCOUNTS.value} VALUES (?, ?, ?)", (self.donor_id, self.email, self.password))   
            
    def alter_row(self, donor_id, column, value):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor() 
            setattr(self, column.value, value)
            c.execute(f"UPDATE {Table.ACCOUNTS.value} SET {column.value} = ? WHERE donor_id = ?", (value, donor_id))
            
        