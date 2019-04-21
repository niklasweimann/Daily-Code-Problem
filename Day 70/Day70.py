def get_perfect_number(k):
    digits = str(k).split()
    sum = 0
    for i in digits:
        sum += int(i)
    digits.append(str(10 - sum))
    return "".join(digits)


print(get_perfect_number(1))
print(get_perfect_number(2))
