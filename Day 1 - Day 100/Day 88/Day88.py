def divide(dividend, divisor, result=None):
    if result is None:
        result = 0
    if dividend < divisor:
        return result
    return divide(dividend - divisor, divisor, result + 1)


for i in range(1, 100):
    for j in range(1, 100):
        if i % j is 0:
            if divide(i, j) is i // j:
                print("{} / {} = {}".format(i, j, divide(i, j)))
            else:
                raise Exception("Error!")
