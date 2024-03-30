#დავ 0
family_members = ["maia", "mari", "qeti"]
print(family_members[0])
print(family_members[1])
print(family_members[2])




#დავ 1
numbers = list(range(1, 11))
print(numbers[0])
print(numbers[-1])

#დავ 2
numbers = list(range(10, 21))
print("Original list items:", numbers)
i = 0
while i < len(numbers):
    numbers[i] = 1
    i += 2
print("Modified list items:", numbers)


#დავ 3
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
location = input("Enter your location: ")
email = input("Enter your email: ")
user_info = [name, surname, age, location, email]
print("User info:", user_info)


#დავ 4
surname = "magradze"
i = 0
while i < len(surname):
    print(surname[i])
    i += 1