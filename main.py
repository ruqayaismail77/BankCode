from methods.deposit import Dep
from methods.withdraw import Wd
from methods.transfer import Tsf

class Bank(Dep, Wd, Tsf):

  def __init__(self):
    super().__init__()
    self.user_name = input("Enter your name : ")
    self.user_password = int(input("Enter your password : "))


  users = [
       {
          'name' : 'saja',
          'id' : '1234567891',
          'password' : 12345,
          'balance' : 0 
       },
       {
          'name' : 'noor',
          'id' : '1234512345',
          'password' : 67890,
          'balance' : 0         
       }
    ]
  def choose():
    print('1. Deposit money')
    print('2. withdraw money')
    print('3. Transfer money')
    print('4. Show balance')
    print("5. Quit")

  def login(self):
    for user in Bank.users:
      if self.user_name.lower() == user['name'] and self.user_password == user['password']:
        self.person1 = user
        while True:
            Bank.choose()
            choose_op = int(input("Choose the operation : "))
            if choose_op == 1:
                print(Dep.deposit(self))
            elif choose_op == 2:
                print(Wd.withdraw(self))
            elif choose_op == 3:
                print(Tsf.transfer(self))
            elif choose_op == 4:
                print(f"balance {self.person1['balance']}")
            elif choose_op == 5:
               break
            else:
                return "Please enter a valid number!"
    else:
      return "wrong user name or password!"


user1 = Bank()
user1.login()
