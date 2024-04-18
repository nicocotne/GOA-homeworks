#დავ 0
def process_name(name):
    if len(name) >= 3:
        print(name[:3])
    else:
        print(name[0])
user_input = input("Enter name: ")
process_name(user_input)

#დავ 1
num0 = []
for i in range(10, 21):
    num0.append(i)
num1 = num0[::2]
print(num1)




#დავ 2
word = input("Enter word: ")
print(word[::-1])