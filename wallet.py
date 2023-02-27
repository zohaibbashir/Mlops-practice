#changes in wallet.py
balance = 0;

class Wallet:
    def __init__(self, amount):
        global balance
        balance = amount;
        
    def addAmount(self, amount):
        global balance
        balance = balance + amount;
    
    def removeAmount(self, amount):
        global balance
        balance = balance - amount;
        
    def getAmount(self):
        global balance
        return balance;
