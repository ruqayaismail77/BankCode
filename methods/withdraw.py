class Wd:
  def __init__(self):
     pass
  
  def withdraw(self):
    amount = float(input("Enter withdraw amount: "))
    while amount > self.person1['balance']:
        print("Balance is not enough")
        amount = float(input("Enter withdraw amount: "))  
    self.person1['balance'] -= amount
    return f"Withdrew done {self.person1['balance']}, withdraw {amount}"