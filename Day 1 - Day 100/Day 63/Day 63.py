def findWord(matrix: list(list()), word: str):
    word_length = len(word)
    first_char = word[0]
    for i in range(0, len(matrix)):
        current_array = matrix[i]
        try:
            index_of_first_letter = current_array.index(first_char)
        except:
            index_of_first_letter = -1
        if index_of_first_letter == -1:
            continue
        # left to right
        if len(current_array) - index_of_first_letter >= word_length:
            word_array_found = current_array[index_of_first_letter: index_of_first_letter + word_length]
            if "".join(word_array_found) == word:
                return True

        # top to bottom
        if len(matrix) - i >= word_length:
            word_array_found = []
            for j in range(0, word_length):
                word_array_found.append(
                    matrix[i+j][index_of_first_letter])

            if "".join(word_array_found) == word:
                return True

    return False


matrix = [['F', 'A', 'C', 'I'],
          ['O', 'B', 'Q', 'P'],
          ['A', 'N', 'O', 'B'],
          ['M', 'A', 'S', 'S']]
print(findWord(matrix, "FOAM"))  # true
print(findWord(matrix, "MASS"))  # true
print(findWord(matrix, "ADFSFSFFSFSF"))  # False
