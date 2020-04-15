class BankAccount:

    def __init__(self):
        self.balance = 0

    def add_money(self, amount):
        """Add money to a bank account

        Arguments:
          amount - A numerical value by which the bank account's balance will increase
        """
        try:
            if amount >= 1:
                self.balance += amount
                print("Your deposit was successful")
            elif amount > 0:
              raise ArithmeticError("Amount was less than 1")
              print("This line will not be executed")
            else:
              raise ArithmeticError("Amount needs to be a positive number")
              
        except TypeError:
            print("Your deposit was not successful because the amount needs to be a number")
        except ArithmeticError as taco:
            print(f"Your deposit was not successful. Error: {taco}")
        
        print("Here is the new balance: ", self.balance)

    def withdraw_money(self, amount):
        """Withdraw money to a bank account

        Arguments:
          amount - A numerical value by which the bank account's balance will decrease
        """
        self.balance -= amount
