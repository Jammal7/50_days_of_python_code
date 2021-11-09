print("Welcome to the rollercoster!")
height = int(input("Input your height in cm: "))

if height >= 120:
    print("You can ride the rollercoster!")
    age = int(input("Input your age: "))
    if age < 12:
        print("Please pay £5.0")
    elif age >= 18:
        print("Please pay £15.0")
    else:
        print("Please pay £7.50")
else:
    print("sorry, you have tp grow taller before you can ride. ")