from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(s):
    nodes = deque()
    for s in s.split('\n'):
		nodes.append(s) # Having each node
    def DeserializeAux():
		val = nodes.popleft()
		if(val == 'empty'):
			return None
		return Node(val, DeserializeAux(), DeserializeAux())
    return DeserializeAux()

def serialize(root):
	if(root is None): return 'empty'
	return root.val + '\n' + serialize(root.left) + '\n' + serialize(root.right)

node = Node('root', Node('left', Node('left.left')), Node('right'))
print('serialize: ' + serialize(node))
assert deserialize(serialize(node)).left.left.val == 'left.left'
