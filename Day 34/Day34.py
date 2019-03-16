import math


def findMinInsertions(str, l, h):
    if (l == h):
        return 0
    elif (l > h):
        return math.inf
    elif (l == h - 1):
        return 0 if(str[l] == str[h]) else 1

    if(str[l] == str[h]):
        return findMinInsertions(str, l + 1, h - 1)
    else:
        return (min(findMinInsertions(str, l, h - 1),
                    findMinInsertions(str, l + 1, h)) + 1)


def isPalindrome(s):
    rev = s[::-1]

    if (s == rev):
        return True
    return False


def insertChars(str, min):
    temp = str
    for i in range(min, -1, -1):
        temp = temp[len(temp) - i: len(temp) - i+1] + temp

    if (isPalindrome(temp)):
        return temp

    temp = str
    for i in range(min-1, -1, -1):
        temp = temp + temp[i: i + 1]

    if (isPalindrome(temp)):
        return temp


def printPol(str):
    minChanges = findMinInsertions(str, 0, len(str) - 1)
    result = insertChars(str, minChanges)
    print(result)


printPol("google")
printPol("race")
