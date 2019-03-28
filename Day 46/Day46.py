def isPalindrome(text):
    if text is None:
        return False
    left = 0
    right = len(text) - 1
    while (left < right):
        if text[left] is not text[right]:
            return False
        left = left + 1
        right = right - 1
    return True


def getSubstrings(string):
    res = []
    for i in range(len(string)):
        res.append(string[i:])
        res.extend(getSubstrings(string[i:i-1]))
    return res


def findLongestPalidrome(string):
    longest = ""
    sub_strings = getSubstrings(string)
    for i in sub_strings:
        if len(i) > len(longest) and isPalindrome(i):
            longest = i
    return longest


print(findLongestPalidrome("aabcdcb"))  # bcdcb
print(findLongestPalidrome("bananas"))  # anana
