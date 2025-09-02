class Tsf:
  def __init__(self):
    pass

  def transfer(self):
    trans_id = input("Enter user ID : ")
    if len(trans_id) == 10:
      for user_id in self.users:
        if trans_id == user_id['id']:
          amountToTransfer = float(input("Enter the amount you want to transfer : "))
          while amountToTransfer > self.person1['balance']:
            print("Balance is not enough")
            amountToTransfer = float(input("Enter the amount you want to transfer : "))
          self.person1['balance'] -= amountToTransfer
          user_id['balance'] += amountToTransfer
          return f'balance {self.person1['balance']}, trans {amountToTransfer}'
    else:
      return "ID must be 10 numbers!"
    