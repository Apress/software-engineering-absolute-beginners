# Import the datetime library
import datetime
"""
Here the function name, calculate_age, reflects what it will be used for. 
The one argument it accepts, year_born, is named after the value you want. 
It should always return an integer due to the return type being specified
"""
def calculate_age(year_born) -> int:
    current_year = datetime.datetime.now().year
    # This function returns a value. Y 
    return (current_year - year_born)

# Here we are calling the function. It returns the age and stores it in the variable 
# called 'age'
age = calculate_age(2000)

# Print age to screen
print(age)
