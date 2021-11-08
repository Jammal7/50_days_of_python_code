monday_temperatures = [9.1, 8.8, 7.6]
def celsius_to_kelvin (cels):
    return cels + 273.15

# for temperature in monday_temperatures:
#     # print(round(temperature))
#     # print(celsius_to_kelvin(temperature))

# Looping through dictionary
# student_grades = {'Marry': 9.1, 'Ola': 8.8, 'Jam': 7.6}
# for grades in student_grades.items():
#     print(grades)

# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
# for pair in phone_numbers.items():
#     print("{} has as phone number {}".format(pair[0], pair[1]))

# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
# for key, value in phone_numbers.items():
#     print("{} has as phone number {}".format(key, value))

# While loops
# username = ''
# while username != 'pypy':
#     username = input("Enter username:")
while True:
    username = input('Enter Username: ')
    if username == 'pypy':
        break
    else:
        continue