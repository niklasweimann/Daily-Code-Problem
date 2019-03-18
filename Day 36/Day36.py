class Node:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        self.locked = False

    def __str__(self):
        return "<" + str(self.val) + ">"

    def _get_root(self, n):
        node = n
        while node.parent is not None:
            node = node.parent
        return node

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.val == key:
            return currentNode
        elif key < currentNode.val:
            return self._get(key, currentNode.left)
        else:
            return self._get(key, currentNode.right)

    def insert(self, data):
        # Compare the new value with the parent node
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data, self)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data, self)
                else:
                    self.right.insert(data)
        else:
            self.val = data

        # Print the tree

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def findSecondLargest(self):
        n = self
        while n.right:
            n = n.right
        n = n.parent
        if n.left is not None:
            return n.left
        else:
            return n

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
                     '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
                      (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
                [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


if __name__ == "__main__":
    root = Node('k')
    root.insert('c')
    root.insert('d')
    root.insert('a')
    root.insert('b')
    root.insert('x')
    root.insert('y')
    root.insert('z')
    root.display()
    print(root.findSecondLargest())
