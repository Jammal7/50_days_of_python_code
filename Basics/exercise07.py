# Loop over the colors items and print out the item in every loop only if the item is greater than 50.
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color > 50:
        print(color)

# Loop over the colors items and print out the item in every loop only if the item is an integer and it is greater than 50.
for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)

# Make the code print out the following output using a for loop:
# John Smith: +37682929928
# Marry Simpons: +423998200919
# So, the code should loop over the dictionary items and in each iteration should print 
# out the dictionary key, a colon, a space, and the corresponding  value.
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key, value in phone_numbers.items():
    print("%s: %s" % (key, value))

# Define a function that takes as a parameter a list that contains both integers and 
# strings and returns the list containing only the integers.
def foo(simp):
    return[i for i in simp if isinstance(i, int)]

# Define a function that takes as parameter list of numbers and returns the list 
# containing only the numbers that are greater than 0.
def foo(numb):
    return[i for i in numb if i > 0]

# Define a function that takes as parameter a list that contains decimal numbers as 
# strings and returns the sum of those numbers.
def foo(dec):
    return sum([float(i) for i in dec])

# Define a function that takes as parameter a list that contains both numbers and 
# strings and returns the same list but with zeros instead of strings.
def foo(bth):
    return[i if not isinstance(i, int) else 0 for i in bth]