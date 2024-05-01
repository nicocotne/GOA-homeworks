# def print_range(start, end):
#     for num in range(start, end + 1):
#         print(num)
# print_range(1, 5)





# def sum(start, end):
#     totaly = 0
#     for num in range(start, end + 1):
#         totaly += num
#     return totaly
# print(sum(1, 5))




# def average(start, end):
#     nums = list(range(start, end + 1))
#     totaly = sum(nums)
#     average = totaly / len(nums)
#     return average
# print(average(1, 5)) 




# def print_letter(name, index):
#     if index < 0 or index >= len(name):
#         print("Index out of range")
#     else:
#         print(name[index])
# print_letter("example", 2)




# def age_classification(age):
#     for _ in range(100):
#         if age < 18:
#             print("You are a baby")
#         elif age < 60:
#             print("You are an adult")
#         else:
#             print("You are a pensioner")
#             break
# age_classification(70)





def print_variable():
    variable = "value of the variable"
    print(variable)
print_variable()
