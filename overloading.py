#overloading
#real life examples

class Payment:
    def make_payment(self,amount):
      print(f'Intiating payment of {amount} ')
      
class CardPayment(Payment):
    def make_payment(self, amount, card_number = None, cvv=None):
        if card_number and cvv:
            print(f'paid {amount} using Card: {card_number}')
        else:
            print(f'missing card details for payment of {amount}')
            
class MobileMoney(Payment):
    def make_payment(self, amount, phone_number=None, password = None):
        if phone_number and password:
            print(f'paid {amount} using Mobile Money: {phone_number}')
        else:
            print(f'missing phone number for payment of {amount}')
            
obj1 = Payment()
obj1.make_payment(10000)

obj2 = CardPayment()
obj2.make_payment(10000, 5354-9336, 192)

obj3 = MobileMoney()
obj3.make_payment(50000,+23245555,9084)