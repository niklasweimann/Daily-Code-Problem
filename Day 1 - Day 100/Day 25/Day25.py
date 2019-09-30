def isMatch(s, p):
    # init matrix with false on every field
    matrix = [[False]*(len(p)+1) for i in range(len(s)+1)]
    matrix[0][0] = True

    # iterate over every field in the matrix
    for i in range(len(s)+1):
        for j in range(1, len(p) + 1):
            # handle star character
            if p[j-1] == '*':
                matrix[i][j] = matrix[i][j-2] or (i > 0 and j > 1 and (
                    p[j - 2] == '.' or s[i - 1] == p[j - 2]) and matrix[i - 1][j])
            # handle . and normal characters
            elif i > 0 and (p[j-1] == '.' or p[j-1] == s[i-1]):
                matrix[i][j] = matrix[i-1][j-1]
    return matrix[len(s)][len(p)]


print(isMatch('', '*'))  # true
print(isMatch('', '.'))  # false
print(isMatch('ray', 'ra.'))  # true
print(isMatch('raymond', 'ra.'))  # false
print(isMatch('chat', '.*at'))  # true
print(isMatch('chats', '.*at'))  # false
print(isMatch('cat', '.*at'))  # true
