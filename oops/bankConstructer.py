class Bank:
    def __init__(self,acno,name,minbalance):
        self.acno=acno
        self.name=name
        self.balance=minbalance
        print("hi")
    def deposit(self,amount):
        self.balance+=amount
        print("acount credited wth amount",amount,"aval balance",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficent balance")
        else:
            self.balance-=amount
            print("acount debited wth amount", amount, "aval balance", self.balance)

obj=Bank(100,"vijay",2000)


