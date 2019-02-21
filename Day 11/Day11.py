array = ["dog", "deer", "deal", "de", "default", "cat", "hamster"]
string = 'de'

def search(prefix, data):
    return filter(lambda x: x.startswith(prefix), data)

print(array)
print(search(string, array))