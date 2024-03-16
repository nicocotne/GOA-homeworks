#დავ 0
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)




#დავ 1
number = float(input("Enter a number: "))
if number > 0:
    print("The entered number is positive")
elif number < 0:
    print("The entered number is negative")
else:
    print("The entered number is zero")


#დავ 2
for i in range(2, 101, 2):
    print(i)


#დავ 3
total = 0
num = 1
while num <= 100:
    total += num
    num += 1
print("Sum of numbers from 1 to 100:", total)



#დავ 4
day_number = int(input("Enter a number for the day of the week: "))
if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid input. Please enter a number between 1 and 7.")


#დავ 5
number = int(input("Enter a number: "))
if number == 0:
    print("The entered number is zero")
elif number % 2 == 0:
    print("The entered number is even")
else:
    print("The entered number is odd")