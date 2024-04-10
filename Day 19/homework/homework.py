# def sum(i, index):
#     try:
#         if index >= 0 and index < len(i):
#             return i[index]
#         else:
#             return "Invalid index!"
#     except TypeError:
#         return "Please enter an integer index!"
# i = [10, 20, 30, 40, 50]
# index = int(input("Enter the index: "))
# result = sum(i, index)
# print("Result:", result)
def sum_two_smallest_numbers(num):
    if len(num) < 2:
        return "List should have at least two elements"
    lst.sort()
    return lst[0] + lst[1]
test_cases = [([5, 8, 12, 18, 22], 13), 
              ([7, 15, 12, 18, 22], 19), 
              ([25, 42, 12, 18, 22], 30)]

for lst, expected_result in test_cases:
    result = sum_two_smallest_numbers(lst)
    print("For list {}, expected result is {}, and got {}".format(lst, expected_result, result))
