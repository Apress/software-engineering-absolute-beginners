class Funds:
    total_expenses = 0
    total = 0
    # Added a variable to hold any error messages we may encounter
    error = '';

    # Constructor. We populate it with the total amount available
    def __init__(self, total):
        self.total = total

    # Sets the money we have spend
    def set_expense(self, expense):
        # Checks whether we have enough money left to give out
        if self.get_funds_left() > expense:
            self.total_expenses += expense
            return True  # Exit the function

        # If we don't, set the error message and return false. Returning false here
        # allows us to detect a failed expense deduction
        self.error = 'Out of funds'
        return False

    # Calculates the amount of money left
    def get_funds_left(self):
        return self.total - self.total_expenses

    # Returns the error
    def get_error(self):
        return self.error

# Code implementation part
funds = Funds(20)

# Check whether the set_expense function returns True or False. Using the 'not'
# keyword indicates false. Then we print the error.
if not funds.set_expense(10):
    print(funds.get_error())

if not funds.set_expense(2):
    print(funds.get_error())

if not funds.set_expense(15):
    print(funds.get_error())

# Prints the amount left to screen
print('You have £' + str(funds.get_funds_left()) + ' left.')
