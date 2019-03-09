def isBalanced(string):
    stack = []
    while string is not "":
        first = string[:1]
        if first is '(':
            stack.append("A")
        elif first is '{':
            stack.append("B")
        elif first is '[':
            stack.append("C")
        elif first is ')':
            if stack[-1:][0] is 'A':
                stack.pop()
            else:
                return False
        elif first is '}':
            if stack[-1:][0] is 'B':
                stack.pop()
            else:
                return False
        elif first is ']':
            if stack[-1:][0] is 'C':
                stack.pop()
            else:
                return False
        string = string[1:]
    return len(stack) is 0


print(isBalanced("([])[]({})"))  # true
print(isBalanced("([)]"))  # false
print(isBalanced("((()"))  # false
print(isBalanced(""))  # true
print(isBalanced("("))  # false
print(isBalanced("()()()()"))  # true
