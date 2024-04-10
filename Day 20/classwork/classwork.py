def sum_even_odd_indices(i):
    sum_even = sum_odd = 0
    for i in range(len(i)):
        if i % 2 == 0:
            sum_even += i[i]
        else:
            sum_odd += i[i]
    i = [sum_even, sum_odd]
    return i
box = [
    ([80], [80, 0]),
    ([100, 50], [100, 50]),
    ([50, 60, 70, 80], [120, 140]),
    ([13, 27, 49], [62, 27]),
    ([70, 58, 75, 34, 91], [236, 92])]
for i, expected_result in box:
    result = sum_even_odd_indices(i)
    print(f"For list {i}, expected result is {expected_result}, and got {result}")
