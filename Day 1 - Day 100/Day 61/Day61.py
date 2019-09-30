def pow(x, y):
    if y is 0:
        return 1
    elif y % 2 is 0:
        c = pow(x, int(y / 2))
        return c * c
    else:
        c = pow(x, int(y/2))
        return x * c * c


max_val = 100
for i in range(0, max_val):
    for j in range(0, max_val):
        res = pow(i, j)
        print(res)
        assert res == i ** j
