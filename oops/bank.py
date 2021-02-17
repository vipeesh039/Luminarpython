class Bank:
    def creat_account(self,acno,name,minbalance):
        self.acno=acno
        self.name=name
        self.balance=minbalance
    def deposit(self,amount):
        self.balance+=amount
        print("acount credited wth amount",amount,"aval balance",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficent balance")
        else:
            self.balance-=amount
            print("acount debited wth amount", amount, "aval balance", self.balance)

obj=Bank()
obj.creat_account(10,"vijay",3000)
obj.deposit(5000)
obj.withdraw(2000)
obj.withdraw(10000)
