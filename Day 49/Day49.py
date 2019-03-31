from math import inf


def get_Max_Sum(arr):
    max_sum_found = -inf
    current_sum = 0
    for i in arr:
        current_sum = current_sum + i
        if max_sum_found < current_sum:
            max_sum_found = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum_found if max_sum_found >= 0 else 0


arr = [34, -50, 42, 14, -5, 86]  # 137
print(get_Max_Sum(arr))

arr = [-5, -1, -8, -9]  # 0
print(get_Max_Sum(arr))

arr = [-5, 1, -8, -9]  # 1
print(get_Max_Sum(arr))

arr = [5, 1, 8, 9]  # 23
print(get_Max_Sum(arr))

arr = [-5, 1, 8, -99]  # 9
print(get_Max_Sum(arr))
