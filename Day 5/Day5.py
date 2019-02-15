def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

## Solution ##


def car(cons):
    def get_first(a, b):
        return a
    return cons(get_first)


def cdr(cons):
    return cons(lambda x, y: y)


print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
