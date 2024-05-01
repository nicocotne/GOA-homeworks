#დავ 0
def sum(nums):
    totaly = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            totaly += nums[i]
    return totaly
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum(nums)
print("Sum of nums at even indices:", result)




#დავ 1
def even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even(2))
print(even(3))


#დავ 2
def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
print(prime(7))
print(prime(10))
#დავ 3
def names(names):
    name = [name() for name in names]
    return name
names = ["david", "chad", "gigachad"]
print(names(names))




#დავ 4
def nums(numbers):
    update_nums = []
    for num in numbers:
        if num % 2 == 0:
            update_nums.append(num * 2)
        else:
            update_nums.append(num // 2)
    return update_nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums(nums))



