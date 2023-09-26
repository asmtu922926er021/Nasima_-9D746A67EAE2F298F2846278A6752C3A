# python program to create bankaccount class
# with both a deposit() and a withdraw() fuction
class Bank_Account:
  def __init__(self):
    self.balance=0
    print("Hello!!! Welcome to the deposit & Withdrawal Machine")
    def deposit (self):
      amount=float(input("enter amount to be deposited:"))
      self.balance += amount
      print("\n amount deposited:",amount)
    def withdraw (self):
             amount = float(input("enter amount to be withdrawn: "))
             if self.balance>=amount:
               self.balance-=amount
               print("\n you withdraw:",amount)
             else:
               print("\n insufficient balance ")
               def display(self):
                 print("\n net available balance=",self. balance)

# driver code

# creating an object of class
s= Bank_Account()

# calling fuctions with that class object
s.deposit()
s.withdraw()
s.display()