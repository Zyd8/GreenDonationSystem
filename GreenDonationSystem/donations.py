
class Donations:

    total_money = 0

    def __init__(self, donation_id=None, money=0):
        self.__donation_id = donation_id
        self.__money = money
        Donations.total_money += money

    def __repr__(self):
        return f"Donations(donation_id={self.donation_id}, money={self.money})"

    @property
    def donation_id(self):
        return self.__donation_id
    
    @donation_id.setter
    def donation_id(self, value):
        self.__donation_id = value

    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self, value):
        if value > 0:
            self.__money = value
        else:
            raise Exception("Must enter a non-zero, non-negative value")
        
    def get_total_money():
        return Donations.total_money



