def find_rooms(times):
    begin = sorted([num[0] for num in times])
    end = sorted([num[1] for num in times])
    rooms = 0
    i = 0
    j = 0
    length = len(times)

    while i < length and j < length:
        if begin[i] > end[j]:
            rooms -= 1
            j += 1
        else:
            rooms += 1
            i += 1
    return rooms


print(find_rooms([(30, 75), (0, 50), (60, 150)]))
