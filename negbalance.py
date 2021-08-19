

class NegativeBalanceError (Exception):
    def __int__(self, message):
        self.message = message


def checkBalance():
    balance = int(input("Enter a number"))
    if(balance < 0 ):
        raise NegativeBalanceError
try:
    checkBalance()
except (NegativeBalanceError):
    print("Negative Balance, enter proper number")