first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
for i in full_name:
    print(i)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
for i in range(0, len(full_name), 2):
    print(full_name[i])

numbers = [1, 2, 3, 4, 6, 7, 8, 9]
if 5 in numbers:
    print("Yes, 5 is in the numbers list.")
else:
    print("No, 5 is not in the numbers list.")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for num in nums:
    if num % 2 == 0:
        sum += num
print("The sum of even nums from 1 to 10 is:", sum)
