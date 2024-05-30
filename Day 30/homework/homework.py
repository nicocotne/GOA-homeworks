#დავ 0
def reverse_and_upper(string):
    reversed_string = string[::-1].upper()
test_case = "VaNo MoTiashvili"
result = reverse_and_upper(test_case)
print(result)



#დავ 1
def categorize_strings(strings):
    odd = []
    even = []

    for string in strings:
        if all(char.isalpha() and char.islower() for char in string):
            odd.append(string.upper())
        elif all(char.isalpha() and char.islower() for char in string):
            even.append(string.upper())
    return odd, even
test_case = ["vano", "davit", "zuka", "yiyliyo"]
odd, even = categorize_strings(test_case)
print("odd =", odd)
print("even =", even)
#დავ 2
def process_strings(strings):
    even_list = []
    odd_list = []

    for string in strings:
        if sum(1 for char in string if char.isalpha()) % 2 == 0:
            even_list.append(string.upper())
        else:
            odd_list.append(string.capitalize())
    return even_list, odd_list
test_case = ["goa_best", "vano", "nesvi", "tskhVarAdzE"]
result_even, result_odd = process_strings(test_case)
print("Even List:", result_even)
print("Odd List:", result_odd)
#დავ 3
def process_strings(strings):
    result_list = []
    for string in strings:
        if string.isupper():
            result_list.append(string.lower())
        elif string.islower():
            result_list.append(string.upper())
        else:
            result_list.append(string)
    return result_list
test_case = ["vano", "DAVIT", "LUKA", "nika"]
result_list = process_strings(test_case)
print("Result List:", result_list)

#დავ 4
def modify_string(string):
    first_char = string[0]
    if first_char.isupper():
        return string.upper()
    else:
        return string.capitalize()
test_case = "vano motiashvili"
result1 = modify_string(test_case[test_case.find("n")])
result2 = modify_string(test_case[test_case.find("m")])
print("Result1:", result1)
print("Result2:", result2)