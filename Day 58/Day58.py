def getIndex(arr: list, k: int):
    return getIndextUtil(arr, k, 0, len(arr)-1)


def getIndextUtil(arr: list, number_to_find: int, start: int, end: int):
    # simple cases
    if arr[start] is number_to_find:
        return start
    if arr[end] is number_to_find:
        return end
    # Split Array
    mid = int((start + end) / 2)
    # another simple case
    if arr[mid] == number_to_find:
        return mid
    # find index by binary search
    idx = -1
    if number_to_find < arr[mid]:
        if arr[mid] > arr[mid + 1]:
            idx = getIndextUtil(arr, number_to_find, mid+1, end)
        else:
            idx = getIndextUtil(arr, number_to_find, start, mid - 1)

    if number_to_find > arr[mid]:
        if arr[mid] > arr[mid + 1]:
            idx = getIndextUtil(arr, number_to_find, start, mid-1)
        else:
            idx = getIndextUtil(arr, number_to_find, mid + 1, end)
    return idx


print(getIndex([13, 18, 25, 2, 8, 10], 8))  # 4
