def max_win(arr):
    max_diff = 0
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            diff = arr[j] - arr[i]
            if (diff > max_diff):
                max_diff = diff
    return max_diff


arr = [9, 11, 8, 5, 7, 10]
print(max_win(arr))  # 5
arr = [99, 1, 99, 1, 2, 10]
print(max_win(arr))  # 98
arr = [0, 0, 0, 1, 0, 0]
print(max_win(arr))  # 5
arr = [5, 4, 3, 2, 1, 0]
print(max_win(arr))  # 0
