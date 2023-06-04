import sqlite3
from enums import *
from donations import Donations

class Trees(Donations):
    
    #unique
    @staticmethod
    def extend_row(current_user):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute(f"INSERT INTO {Table.TREES.value} VALUES (?, NULL, NULL, NULL)", (current_user,))
            
    # overriden
    @staticmethod
    def init_db():
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS trees (
                        donor_id INTEGER PRIMARY KEY,
                        money real,
                        tree_species text,
                        tree_species_quantity integer
                    )""")
    
    # overriden 
    @staticmethod
    def read_row(donor_id):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute(f"SELECT * FROM {Table.TREES.value} WHERE donor_id = ?", (donor_id,))
            row = c.fetchone()
            if row:
                object = Trees(row[0], row[1], row[2])
                return object
            print("Record not found")
            
    # overriden
    @staticmethod
    def del_row(donor_id):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute(f"DELETE FROM {Table.TREES.value} WHERE donor_id = {donor_id}")
        
    # overriden
    @staticmethod
    def read_table(base, order):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            list = c.execute(f"SELECT * FROM {Table.TREES.value} ORDER BY {base.value} {order.value}")
            for item in list:
                print(item)
    
    # overriden    
    @staticmethod
    def del_table():
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor()
            c.execute(f"DROP TABLE {Table.TREES.value}")
            
    # overriden
    def alter_row(self, donor_id, column, value):
        with sqlite3.connect("GreenDonation.db") as conn:
            c = conn.cursor() 
            setattr(self, column.value, value)
            c.execute(f"UPDATE {Table.TREES.value} SET {column.value} = ? WHERE donor_id = ?", (value, donor_id))

    
    def __init__(self, donation_id=None, money=0, tree_species="", tree_species_quantity=0):
        super().__init__(donation_id, money)
        self.__tree_species = tree_species
        self.__tree_species_quantity = tree_species_quantity

    def __repr__(self):
        return f"Trees(donation_id={self.donation_id}, money={self.money}, tree_species={self.tree_species}, tree_species_quantity={self.tree_species_quantity})"

    @property 
    def tree_species(self):
        return self.__tree_species
    
    @tree_species.setter
    def tree_species(self, value):
        self.__tree_species = value

    @property 
    def tree_species_quantity(self):
        return self.__tree_species_quantity
    
    @tree_species_quantity.setter
    def tree_species_quantity(self, value):
        self.__tree_species_quantity = value


    

        

