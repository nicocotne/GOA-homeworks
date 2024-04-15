# name = "cotne"
# reversed_name = ""
# for index in range(len(name)-1,-1,-1):
#     reversed_name += name[index]

# if name == reversed_name:
#     print(name,"name is palindrome")
# else:
#     print(name,"name is not palindrome")





import math
def square(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        root0 = (-b + math.sqrt(D)) / (2*a)
        root = (-b - math.sqrt(D)) / (2*a)
        return root0, root
    elif D == 0:
        root = -b / (2*a)
        return root, root
    else:
        part = -b / (2*a)
        IDK = math.sqrt(abs(D)) / (2*a)
        root0 = complex(part, IDK)
        root = complex(part, -IDK)
        return root0, root