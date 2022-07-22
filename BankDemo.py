class Bank:

    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello ",self.cname,", Your Account Number ",self.acno," Is Opened With ",self.balance," Rs.")

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("Sorry You Need Another ",amount-self.balance," Rs.")

    def checkBalance(self):
        print("Current Balance : ",self.balance)

b1=Bank()
acno=int(input("Enter Account Number:"))
cname=input("Enter Customer Name:")
balance=int(input("Enter Initial Balance:"))

b1.openAccount(acno,cname,balance)

while True:

    print("*"*50)
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*50)
    
    choice=int(input("Enter Your Choice:"))

    if choice==1:
        amount=int(input("Enter Deposit Amount:"))
        b1.deposit(amount)
        print("*"*50)
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount:"))
        b1.withdraw(amount)
        print("*"*50)
    elif choice==3:
        b1.checkBalance()
        print("*"*50)
    else:
        break


