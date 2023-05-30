from donation import Donation

class Trees(Donation):
    
    def __init__(self, donation_id=None, money=0, species="", quantity=0):
        super().__init__(donation_id, money)
        self.__species = species
        self.__quantity = quantity

    @property 
    def species(self):
        return self.__species
    
    @species.setter
    def species(self, value):
        self.__species = value

    @property 
    def quantity(self):
        return self.__quantity
    
    @species.setter
    def quantity(self, value):
        self.__quantity = value


    

        

