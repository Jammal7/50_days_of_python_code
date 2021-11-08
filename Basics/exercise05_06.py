# Your task for this exercise is to create a calculate_length function that calculates and returns the number of items for any given lst list.
def calculate_length(lst):
    return len(lst)

# Define a function that calculates the area of a square.
def area(square):
    area_of_a_sq = square * square
    return(area_of_a_sq)

# Define a function that converts fluid ounces to milliliters knowing that 1 fluid ounce is equal to 29.57353 milliliters.
def convert(ml):
    return ml * 29.57353

# print(convert(5))

# Define a function that:
# (1) takes a string as parameter
# (2) returns False if the string contains less than 8 characters
# (3) returns True if the string contains 8 or more characters
def character(password):
    if len(password) >= 8:
        return True
    else:
        return False

# Define a function that:
# (1) takes a temperature as parameter
# (2) returns Warm if the temperature is greater than 7
# (3) returns Cold if the temperature is equal or less than 7
def char(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

# Define a function that:
# (1) takes a temperature as parameter
# (2) returns Hot if the temperature is greater than 25
# (3) returns Warm if the temperature is between 15 and 25, including 15 and 25.
# (4) returns Cold if the temperature is less than 15.
def para(temperature):
    if temperature > 25:
        return "Hot"
    elif 25 >= temperature >= 15:
        return "Warm"
    else:
        return "Cold"

# Implement a function that gets a person's name (e.g. john) as a parameter and returns a greeting (e.g. Hi John). 
# Note that the first letter of the person's name should always be uppercase.
name = input("Enter your Firstname: ")
message = f"Hi {name.title()}"
print(message)