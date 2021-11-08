def area(a, b):
    return a * b
# print(area(10, 5))

# Positon arguments
print(area(b=4, a=5))

# default parameters
def subv(a, b=6):
    return a + b
print(subv(4))