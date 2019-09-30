def breakTextUtil(text: str, k: int, arr):
    # Remove leading space
    if text[:1] is " ":
        text = text[1:]
    # If text is empty we could split the whole text
    if not text:
        return arr
    text_array = text.split(sep=" ")
    result = ""

    if len(text_array) is 1 and len(text_array[0]) <= k:
        arr.append(text_array[0])
        return breakTextUtil("", k, arr)
    elif len(text_array) is 1:
        return None
    else:
        for i in text_array:
            if len(result) + len(i) < k:
                if len(result) > 0:
                    result = result + " "
                result = result + i
            elif len(result) > 0:
                arr.append(result)
                break
            else:
                return None
        return breakTextUtil(text[len(result):], k, arr)


def breakText(text: str, k: int):
    return breakTextUtil(text, k, [])


# ['the quick', 'brown fox', 'jumps over', 'the lazy', 'dog']
print(breakText("the quick brown fox jumps over the lazy dog", 10))
# None
print(breakText("the quick brown fox jumps over the lazy dog", 2))
