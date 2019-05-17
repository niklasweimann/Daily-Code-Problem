def get_permutations(data):
    if len(data) <= 1:
        yield data
    else:
        for perm in get_permutations(data[1:]):
            for i in range(len(data)):
                # nb data[0:1] works in both string and list contexts
                yield perm[:i] + data[0:1] + perm[i:]


for i in get_permutations([1, 2, 3]):
    print(i)
