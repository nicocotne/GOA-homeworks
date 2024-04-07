def sum(i, index):
    try:
        if index >= 0 and index < len(i):
            return i[index]
        else:
            return "Invalid index!"
    except TypeError:
        return "Please enter an integer index!"
i = [10, 20, 30, 40, 50]
index = int(input("Enter the index: "))
result = sum(i, index)
print("Result:", result)