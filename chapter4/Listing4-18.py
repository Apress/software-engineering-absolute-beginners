class Funds:
    # These two variables are in the class scope. Initialised to 0
    total_expenses = 0
    total = 0

    # Constructor. We populate it with the total amount available when we
    # construct the object
    def __init__(self, total):
         self.total = total

    # Stores the money we have spend
    def set_expense(self, expense):
          self.total_expenses += expense

    # Calculates the amount of money we have left
    def get_funds_left(self):
         return self.total - self.total_expenses

# Code implementation part. Note that you do not have to put 'self' when calling the
# functions
funds = Funds(200)
funds.set_expense(10)
funds.set_expense(15)
# Prints the amount left to screen
print(funds.get_funds_left())
