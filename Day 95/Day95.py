def find_highest_index(data):
    for i in range(0, len(data)-1):
        if data[i] < data[i + 1]:
            return i + 1
    return False


def next_greater_permutation(data):
    i = find_highest_index(data)
    if not i:
        return sorted(data)
    else:
        i = len(data) - 1
        while i > 0 and data[i - 1] >= data[i]:
            i -= 1

        j = len(data) - 1

        while data[j] <= data[i - 1]:
            j -= 1

        temp = data[i - 1]
        data[i - 1] = data[j]
        data[j] = temp

        j = len(data) - 1

        while i < j:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
            i += 1
            j -= 1
    return data


print(next_greater_permutation([1, 2, 3]))  # [1,3,2]
print(next_greater_permutation([1, 3, 2]))  # [2,1,3]
print(next_greater_permutation([3, 2, 1]))  # [1,2,3]
