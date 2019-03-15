def median(lst):
    n = len(lst)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(lst)[n//2]
    else:
        return sum(sorted(lst)[n//2-1:n//2+1])/2.0


listItem = []
listItem.append(2)
print(median(listItem))
listItem.append(1)
print(median(listItem))
listItem.append(5)
print(median(listItem))
listItem.append(7)
print(median(listItem))
