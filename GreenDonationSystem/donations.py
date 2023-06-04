import sqlite3
from enums import *
from accounts import Accounts

class Donations():

    total_money = 0
    
    # unique
    @staticmethod
    def get_total_money():
        return print(Donations.total_money)
    
    # unique
    @staticmethod
    def extend_row(current_user):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute(f"INSERT INTO {Table.DONATIONS.value} VALUES (?, NULL)", (current_user,))
    
    # overriden
    @staticmethod
    def init_db():
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS donations (
                donor_id INTEGER PRIMARY KEY,
                money real
            )""")
    
    # overriden 
    @staticmethod
    def read_row(donor_id):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute(f"SELECT * FROM {Table.DONATIONS.value} WHERE donor_id = ?", (donor_id,))
            row = c.fetchone()
            if row:
                object = Donations(row[0], row[1])
                return object
            print("Record not found")
            
    # overriden
    @staticmethod
    def del_row(donor_id):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute(f"DELETE FROM {Table.DONATIONS.value} WHERE donor_id = {donor_id}")
        
    # overriden
    @staticmethod
    def read_table(base, order):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            list = c.execute(f"SELECT * FROM {Table.DONATIONS.value} ORDER BY {base.value} {order.value}")
            for item in list:
                print(item)
    
    # overriden    
    @staticmethod
    def del_table():
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute(f"DROP TABLE {Table.DONATIONS.value}")
            
    # overriden
    def alter_row(self, donor_id, column, value):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor() 
            setattr(self, column.value, value)
            c.execute(f"UPDATE {Table.DONATIONS.value} SET {column.value} = ? WHERE donor_id = ?", (value, donor_id))


    def __init__(self, donor_id=None, money=0):
        self.__donor_id = donor_id
        self.__money = money
        Donations.total_money += money

    def __repr__(self):
        return f"Donations(donor_id={self.donor_id}, money={self.money})"

    @property
    def donor_id(self):
        return self.__donor_id
    
    @donor_id.setter
    def donor_id(self, value):
        self.__donor_id = value

    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self, value):
        if value > 0:
            self.__money = value
        else:
            raise Exception("Must enter a non-zero, non-negative value")


