age = int(input("Enter your age: "))
if age <= 0 or age < 18:
    print("User is a child.")
elif age >= 18 and age < 50:
    print("User is an adult.")
else:
    print("User is elderly.")