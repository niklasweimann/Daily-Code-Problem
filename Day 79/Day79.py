def get_count(data):
    joker = True
    for i in range(0, len(data)-1):
        if data[i] > data[i + 1] and joker:
            joker = False
        elif data[i] > data[i + 1]:
            return False
    return True


array = [10, 5, 7]
print(get_count(array))  # true
array = [10, 5, 1]
print(get_count(array))  # false
