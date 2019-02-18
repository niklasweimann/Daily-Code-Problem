from node import Node
# Solution


def count(root):
    if root == None:
        return (0, True)
    left_count, is_left_unival = count(root.left)
    right_count, is_right_unival = count(root.right)
    is_unival = True
    if not is_left_unival or not is_right_unival:
        is_unival = False
    if root.left != None and root.left.data != root.data:
        is_unival = False
    if root.right != None and root.right.data != root.data:
        is_unival = False
    if is_unival:
        return (left_count + right_count + 1, True)
    else:
        return (left_count + right_count, False)


root = Node('a')
root.insert('a')
root.insert('b')
root.insert('a')
root.display()
number, is_unival = count(root)
print(number)
