def sentence(wordList, string, result):
    if len(string) == 0:
        return result.append([])
    for word in wordList:
        if string.startswith(word):
            result[len(result)-1].append(word)
            sentence(wordList, string[len(word):], result)
    return result[:-1]

words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
string = "bedbathandbeyond"
print(sentence(words, string, [[]]))