#დავ 0
def manual_index(numbers_list, search_value):
    # ცვლადი, რომელიც ინახავს მიმდინარე ინდექსს
    index = 0
    # ვატარებთ `for` ციკლს, რომ გადავიდეთ ყველა ელემენტზე სიაში `numbers_list`
    for number in numbers_list:
        # თუ მიმდინარე ელემენტი ტოლია `search_value`-ს
        if number == search_value:
            # აბრუნებს მიმდინარე ინდექსს
            return index
        # ინდექსს ერთი ერთით ვზრდით ყოველი ელემენტის შემოწმების შემდეგ
        index += 1
    # თუ ელემენტი არ მოიძებნა სიაში, აბრუნებს -1-ს
    return -1
# ტესტი
numbers_list = [10, 20, 30, 40, 50]
search_value = 30
print(manual_index(numbers_list, search_value))  # უნდა დააბრუნოს 2, რადგან 30-ის ინდექსია 2

#დავ 1
def manual_max(numbers_list):
    # თუ სია ცარიელია, აბრუნებს None-ს
    if not numbers_list:
        return None
    # ცვლადი, რომელიც ინახავს მაქსიმალურ მნიშვნელობას, ინიციალიზებულია პირველი ელემენტით
    max_value = numbers_list[0]
    # ვატარებთ `for` ციკლს, რომ გადავიდეთ ყველა ელემენტზე სიაში `numbers_list`
    for number in numbers_list:
        # თუ მიმდინარე ელემენტი მეტი არის max_value-ზე, ვანახლებთ max_value-ს
        if number > max_value:
            max_value = number
    # აბრუნებს მაქსიმალურ მნიშვნელობას
    return max_value
def manual_min(numbers_list):
    # თუ სია ცარიელია, აბრუნებს None-ს
    if not numbers_list:
        return None
    # ცვლადი, რომელიც ინახავს მინიმალურ მნიშვნელობას, ინიციალიზებულია პირველი ელემენტით
    min_value = numbers_list[0]
    # ვატარებთ `for` ციკლს, რომ გადავიდეთ ყველა ელემენტზე სიაში `numbers_list`
    for number in numbers_list:
        # თუ მიმდინარე ელემენტი ნაკლები არის min_value-ზე, ვანახლებთ min_value-ს
        if number < min_value:
            min_value = number
    # აბრუნებს მინიმალურ მნიშვნელობას
    return min_value
numbers_list = [10, 20, 30, 40, 50]# ტესტი
print(manual_max(numbers_list))  # უნდა დააბრუნოს 50, რადგან ეს არის მაქსიმუმი
print(manual_min(numbers_list))  # უნდა დააბრუნოს 10, რადგან ეს არის მინიმუმი
#დავ 2
def manual_pop(numbers_list, index):
    # თუ ინდექსი არასწორია (მეტია სიის სიგრძეზე ან ნაკლებია 0-ზე), აბრუნებს None-ს
    if index < 0 or index >= len(numbers_list):
        return None
    # ახალი სია, რომელიც იქნება გამოსაბრუნებელი შედეგი
    new_list = []
    # ვატარებთ `for` ციკლს, რომ გადავიდეთ ყველა ელემენტზე სიაში `numbers_list` ინდექსით
    for i in range(len(numbers_list)):
        # თუ მიმდინარე ინდექსი არ ემთხვევა წასაშლელ ინდექსს, ვამატებთ ელემენტს ახალ სიაში
        if i != index:
            new_list.append(numbers_list[i])
    # აბრუნებს ახალ სიას
    return new_list
# ტესტი
numbers_list = [10, 20, 30, 40, 50]
index_to_remove = 2
print(manual_pop(numbers_list, index_to_remove))  # უნდა დააბრუნოს [10, 20, 40, 50], რადგან 30 (ინდექსი 2-ზე) წაშლილია
