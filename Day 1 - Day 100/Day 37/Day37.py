def powerSet(list):
    result = [[]]
    for i in list:
        result.extend([subset + [i] for subset in result])
    return result


set = [1, 2, 3]
print(powerSet(set))
