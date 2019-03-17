def swap(item1, item2, list):
    temp = list[item1]
    list[item1] = list[item2]
    list[item2] = temp
    return list

def isLess(item1, item2, temp):
    sortlist = ['R', 'G', 'B']
    index1 = temp[item1]
    index2 = temp[item2]
    if(sortlist.index(index1) < sortlist.index(index2)):
        return True
    return False

def sort(list):
    temp = list
    for i in range(0, len(temp)-1):
        for j in range(0, len(temp)-1):
            if(not isLess(j, j+1, temp)):
                temp = swap(j, j+1, temp)
    return temp
array = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(sort(array))