def depth(path_str):
    stack = [(-1, 0)]
    max_len = 0
    for p in path_str.split("\n"):
        depth = p.count('\t')
        p = p.replace('\t', '')
        while stack and depth <= stack[-1][0]:
            stack.pop()
        if '.' not in p:
            stack.append((depth, len(p) + stack[-1][1] + 1))
        else:
            max_len = max(max_len, len(p) + stack[-1][1])
    return max_len


print(depth("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
print(depth(
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
print(depth(
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tparent\n\t\tsubdir2\n\t\t\tsubsubdir2\n\t\t\t\tfile2.ext\n\t\tchild.as"))
