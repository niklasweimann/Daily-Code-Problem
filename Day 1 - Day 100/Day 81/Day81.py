def get_possible_words(data, number):
    input = str(number)
    res = ['']
    for char in input:
        if char not in data.keys():
            return None
        letters = data.get(int(char), '')
        res = [prefix+letter for prefix in res for letter in letters]
    return res


numpad = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"]
}
print(get_possible_words(numpad, "213"))
