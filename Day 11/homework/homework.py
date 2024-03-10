#დავ 1
for i in range(0, 51, 5):
    print(i)

#დავ 2
for i in range(2, 22, 2):
    print(i)


#დავ 3
for i in range(5,11):
    print(i*i)


#დავ 4
i = int(input("Enter your number: "))
num = 1
for i in range(2,i+1):
    num *= i
print(num)




#დავ 5
num = int(input("Enter number: "))
result = 0

while num != 0:
    if num % 2 == 0:
        result += num // 2
    else: 
        result += (num * 3) + 1
    num = int(input("Enter a new number: "))
print("result: ")



#დავ 6
num = 10
while num >= 1:
    print(num)
    num -= 1

#დავ 7
name = input("please enter your name: ")
while name.lower() != "quit":
    print("your name is:", name)
    name = input("Ask you to enter your name, or to collect the next good one: ")
#დავ 8
num = 10
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1




#დავ 9
num = int(input("Enter number: "))
while num >= 0:
    num = int(input("Enter number: "))

#დავ 10
num = 1
while num <= 10:
    print(num ** 2)
    num += 1
