string = "111"
validSubStrings = []


def decode(digits):
    n = len(digits)
    count = [0] * (n+1)
    count[0] = 1
    count[1] = 1

    for i in range(2, n+1):
        count[i] = 0
        if int(digits[i - 1]) in range(1, 9):
            count[i] = count[i-1]
        if int(str(digits[i-2])+str(digits[i-1])) in range(10, 26):
            count[i] += count[i-2]
    return count[n]


print(decode(string))
