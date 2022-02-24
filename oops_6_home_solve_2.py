class Account:

    def __init__(self,owner,balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):

        self.balance = self.balance + dep_amt
        print(f"Added {dep_amt} is added to the balance")

    def withdrawl(self,wd_amt):

        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print("Withdrawl Accepted")
        else:
            print("Sorry Not enough funds!!")
        # print(f"Debited {wd_amt} from the balance")

    def _str_(self):
        return f"Owner : {self.owner} \nBalance : {self.balance}"

    
a = Account("Akshay", 500)
print(a.balance)
a.withdrawl(50)
print(a.balance)
print(a)