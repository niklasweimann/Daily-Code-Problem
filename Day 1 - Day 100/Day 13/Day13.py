def getSubstring(chars, string):
    diff = 1
    longest = ['']
    k = 0
    for i in range(0, len(string)):
        for j in range(i, len(string)):
            if string[j] in str(longest[k]):
                longest[k] += string[j]
            elif diff < chars:
                diff += 1
                longest[k] += string[j]
            else:
                break
        diff = 0
        k += 1    
        longest.append('')
    return max(longest, key=len) 

print(getSubstring(2, "aaaaaaaaaabccdddddba"))