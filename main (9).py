"""Implement a class called BankAccount that represents a bank account.The class should have private
attributes for account number,account holder name,and account balance.
deposit money,wihdraw money,and display the account balance.Ensure that the account balance 
Cannot be accessed directly from outside the class.write a program to create an instance of the 
BankAccount class and test the deposit and withdrawal functionality."""


class BankAccount:

  def__inif__(self,account number,account_holder_name,initial_balance=0.0):
  self.__account_number = account_number
  self.__account_holder_name = account_holder_name
  self.__account_balance = initial_balance

  def deposit(self,account):
    if amount>0:
      self.__account_balance += amount 
      #self.__account_balance = self.__account_balance+amount 
      print("Deposited ₹{}.New balance: ₹{}".format(amount,self.__account.balance))

    else:
      printprint("Invalied deposit amount.")

  def withdrawwithdraw(self,amount):
    if amount>0 and amount<=self.__account_balance:
       self.__account_balance-= amount 
       #self.__account_balance = self.__account_balance-amount 
         print("withdraw ₹{}.New balance: ₹ {}".format(amount,self.__account_balance))

    else:
      print("Invalied withdrawal amount or insufficient balance.")

  def display_balance(self):
    print("Account balance for {} (Account #{}): ₹{}".format(self.__account_holder_name,self.__number,self.__account_balance))




#Create an inside of the BankAccount class 
account = BankAccount(account_number="123456789",account_holder_name="Hari prabu",initial_balance=5000.0)



#Test deposit and withdrawal functionality 
 account.display_balance()
 account.deposiy(500.0)
 account.withdraw(200.0)
 account.withdraw(20000.0)
 account.display_balance()

