class bank_account():
    def __init__(self,nr):
        self.account=nr
        self.balance=0
    def show_info(self):   
        print("Rachunek nr: {} {} {} {} {} {} {}".format(self.account[0:2],self.account[2:6],self.account[6:10],self.account[10:14],self.account[14:18],self.account[18:22],self.account[22:26]))
        print("Saldo: {} zł ".format(self.balance))
    def deposite(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount    
        else:
            print("Niewystarczjąca ilość środków na rachunku")     
konto=bank_account("12345655559090111100007722")     
konto.show_info()  
konto.deposite(25.30)  
konto.show_info() 
konto.withdraw(31.70)
konto.show_info()
konto.withdraw(14)  
konto.show_info()
