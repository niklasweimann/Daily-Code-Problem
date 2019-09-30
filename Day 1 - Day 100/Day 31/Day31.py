def changeScore(from_string, to_string):
    from_string_len = len(from_string)
    to_string_len = len(to_string)
    A = [[-1] * from_string_len for i in range(to_string_len)]

    for i in range(from_string_len):
        A[0][i] = i

    for j in range(from_string_len):
        A[j][0] = j

    for i in range(1, to_string_len):
        for j in range(1, from_string_len):
            if from_string[j - 1] == to_string[i - 1]:
                A[i][j] = A[i - 1][j - 1]
            else:
                A[i][j] = min(
                    A[i - 1][j] + 1,
                    A[i][j - 1] + 1,
                    A[i - 1][j - 1] + 1
                )
    return A[to_string_len - 1][from_string_len - 1]


print(changeScore("kitten", "sitting"))  # should be 3
