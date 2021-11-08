def mean(mylist):
    if type(mylist) == dict:
        the_mean = sum(mylist.values()) / len(mylist)
    else:
        the_mean = sum(mylist) / len(mylist)
    return the_mean



# if conditionals
monday_tempt = [8.8, 6.8, 3.4]
student_grades = { 'Marry': 9.2, 'Sam': 10.5, 'Olu': 8.8}
# print(mean(student_grades))
# print(mean(monday_tempt))

# user inputs
def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

# user_input = float(input("Enter temperature: "))
# print(weather_condition(user_input))

# String formatting
user = input("Enter Firstname: ")
surname = input("Enter Surname: ")
when = "today"
# message = "Hello %s %s" % (user, surname)
message = f"Hello {user} {surname} . What's up {when}"
print(message)
