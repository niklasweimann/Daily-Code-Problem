array = [2, 4, 6, 2, 5]  # [5, 1, 1, 5]


def maxSum(list):
    if len(list) < 1:
        return 0
    elif len(list) <= 2:
        return max(list)

    last = list[-1]
    withLast = maxSum(list[:-2]) + last
    withoutlast = maxSum(list[:-1])
    return max(withLast, withoutlast)


print(maxSum(array))
