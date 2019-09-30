def howMuchTimesX(N, X):
    divider = []
    for i in range(1, N+1):
        if X % i is 0 and int(X/i) <= N:
            divider.append(i)
    return len(divider)


N = 6
X = 16
print(howMuchTimesX(N, X))
