class Accounts:
    
    def __init__(self, donation_id=None, email="", password=""):
        self.__donation_id = donation_id
        self.__email = email
        self.__password = password
        
    def __repr__(self):
        return f"Accounts(donation_id={self.donation_id}, email={self.email}, password={self.password})"
    
    @property
    def donation_id(self):
        return self.__donation_id
    
    @donation_id.setter
    def donation_id(self, value):
        self.__donation_id = value  
    
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