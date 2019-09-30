def get_increasing_subsequence(num_list):
    if not num_list:
        return 0
    result = [1] * len(num_list)
    for i in range(1, len(num_list)):
        for j in range(i):
            if num_list[i] > num_list[j]:
                result[i] = max(result[i], result[j] + 1)
    return max(result)

num_list = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(get_increasing_subsequence(num_list))
