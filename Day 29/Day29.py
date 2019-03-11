def encode(string_to_encode):
    result = ""
    first = string_to_encode[0:1]
    count = 0
    while string_to_encode:
        if first is string_to_encode[1:2]:
            count = count + 1
        else:
            count = count + 1
            result = result + str(count) + first
            count = 0
        string_to_encode = string_to_encode[1:]
        first = string_to_encode[0:1]
    return result


def decode(string_to_decode):
    composite_list = [string_to_decode[x:x+2]
                      for x in range(0, len(string_to_decode), 2)]
    result = ""
    for i in composite_list:
        for j in range(0, int(i[0])):
            result = result + i[1]
    return result


string = "AAAABBBCCDAAAAZZZHHHH"
encoded = encode(string)
print("String: " + string)
print("#"*(len(string) + 9))
print("Encoded: " + encoded)
print("Decoded: " + decode(encoded))
