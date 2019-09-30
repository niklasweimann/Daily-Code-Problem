def is_one_or_zero(x, y, b):
    return x * b + y * abs(b-1)


print(is_one_or_zero(2, 3, 1))  # 2
print(is_one_or_zero(2, 3, 0))  # 3
