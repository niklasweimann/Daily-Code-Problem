# i in the first loop finishes looping at 9
# so i = 9 in the second loop and since
# the lambda function is using i, when its
# invoced it only prints 9s
functions = []
for i in range(10):
    functions.append((lambda: i))

i = 1
for f in functions:
    print(f())
    i += 1
