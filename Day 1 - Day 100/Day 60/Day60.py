def isSubsetSum(arr, length, sum):
    if sum == 0:
        return True
    if length == 0 and sum != 0:
        return False
    if arr[length-1] > sum:
        return isSubsetSum(arr, length-1, sum)
    return isSubsetSum(arr, length-1, sum) or isSubsetSum(arr, length-1, sum-arr[length-1])


def calc2Sums(arr):
    # if sum is odd there cannot be a solution
    if sum(arr) % 2 != 0:
        return False
    return isSubsetSum(arr, len(arr), sum(arr) / 2)


# [15, 5, 10, 15, 10] and [20, 35]=>  True
print(calc2Sums([15, 5, 20, 10, 35, 15, 10]))
print(calc2Sums([15, 5, 20, 10, 35]))  # False
