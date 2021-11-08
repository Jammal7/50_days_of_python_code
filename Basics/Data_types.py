# print(24 * 7)

day_hours = 24
week_days = 7
x = 10
y = "10"

sum1 = x + x
sum2 = y + y
# print(day_hours * week_days)
# print(sum1, sum2)

# Range
list(range(1, 10, 2))

# List
student_grades = [9.5, 8, 15, 12, 18, 20]

# Attributes
mysum = sum(student_grades)
length = len(student_grades)
max_value = max(student_grades)
mean = mysum / length
# print(mean)
# print(max_value)

# Dictionary
test_scores = {"Marry": 9.5, "Olu": 8, "Dave": 15, "Tomi": 12}
 
#  Tuples
monday_tempt = (1, 4, 6, 9)

# append
updates = student_grades.append(6)
# print(updates)

# List comprehension
temps = [221, 234, 340, -9999, 230]

# new_temps = [temp / 10 for temp in temps]
# new_temps = [temp / 10 for temp in temps if temp != -9999]
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]
# print(new_temps)










