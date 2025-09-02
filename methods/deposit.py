class Dep:
  def __init__(self):
    pass

  def deposit(self):
    amount = float(input("Enter the amount you want to deposit : "))
    while amount < 1000:
      amount = float(input("Enter the amount you want to deposit : "))

    self.person1['balance'] += amount
    return f"Deposit done {self.person1['balance']}"