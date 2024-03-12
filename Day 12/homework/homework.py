#დავ 0
budget = float(input("enter budget: "))
price = float(input("enter price: "))

if budget >= price:
    print("It is possible to buy")
else:
    print("It is not possible to buy")

#დავ 1
correct_password = "mypassword"
attempts = 0
while attempts < 5:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Password correct!")
        break
    else:
        attempts += 1
        print("Incorrect password.")
        if attempts == 5:
            print("System is blocked.")
            break
        print(f"You have {5 - attempts} attempts left.")
#დავ 2
min_value = int(input("Enter the minimum value for the loop: "))
max_value = int(input("Enter the maximum value for the loop: "))
step = int(input("Enter the step value for the loop: "))
print(f"Looping from {min_value} to {max_value} with a step of {step}:")
for i in range(min_value, max_value + 1, step):
    print(i)



#დავ 3
page1 = input("Enter the first page of the triangle: ")
page2 = input("Enter the second page of the triangle: ")
page3 = input("Enter the third page of the triangle: ")
while not page1.isdigit() or not page2.isdigit() or not page3.isdigit():
    print("Invalid input. Please enter numbers only.")
    page1 = input("Enter the first page of the triangle: ")
    page2 = input("Enter the second page of the triangle: ")
    page3 = input("Enter the third page of the triangle: ")
print("Triangle sides are correct.")
#დავ 4
min_value = int(input("Enter the minimum value for the loop: "))
max_value = int(input("Enter the maximum value for the loop: "))
print(f"Prime numbers between {min_value} and {max_value}:")
for num in range(min_value, max_value + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)


#დავ 5
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return ("Error! Division by zero is not allowed.")
    else:
        return x / y
while True:
    choice = input("Enter choice (1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        break
    else:
        print("Invalid Input")


#დავ 6
while True:
    number = int(input("Enter a number: "))
    if number == 2 or number == 3:
        print("The number is prime.")
        break
    elif number % 2 == 0 or number % 3 == 0:
        print("The number is not prime.")
        break
    else:
        print("Please enter a number that is either 2 or 3.")




#დავ 7
year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")




#დავ 8
import math
a = float(input("Enter the length of the first leg: "))
b = float(input("Enter the length of the second leg: "))
c = math.sqrt(a**2 + b**2)
print("The hypotenuse is:", c)




#დავ 9
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to participate in the selection.")
else:
    print("You are not eligible to participate in the selection.")