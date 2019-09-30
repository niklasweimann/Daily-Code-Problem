class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "<" + str(self.value) + ">"


class Tree:
    def __init__(self):
        self.root = None

    def Get_Root(self):
        return self.root

    def Find_Value(self, data):
        next_node = self.root
        for i in range(0, 1000):
            if data is next_node.value:
                return next_node.value
            if (data < next_node.value):
                if (not next_node.left):
                    return None
                next_node = next_node.left
            elif (data > next_node.value):
                if (not next_node.right):
                    return None
                next_node = next_node.right

    def Insert(self, data):
        if not self.root:
            self.root = Node(data)
        next_node = self.root
        for i in range(0, 1000):
            if (data < next_node.value):
                if (not next_node.left):
                    next_node.left = Node(value=data)
                    return True
                next_node = next_node.left
            elif (data > next_node.value):
                if (not next_node.right):
                    next_node.right = Node(value=data)
                    return True
                next_node = next_node.right

    def Display(self):
        if not self.root:
            print("<Tree is empty>")
            return
        lines, _, _, _ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % node
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % node
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % node
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

    def Clear(self):
        self.root = None

    def Insert_InOrder_and_PreOrder_Helper(self, preorder, inorder):
        if inorder and preorder:
            ind = inorder.index(preorder.pop(0))
            root = Node(inorder[ind])
            root.left = self.Insert_InOrder_and_PreOrder_Helper(
                preorder, inorder[0:ind])
            root.right = self.Insert_InOrder_and_PreOrder_Helper(
                preorder, inorder[ind+1:])
            return root

    def Insert_InOrder_and_PreOrder(self, pre, ino):
        self.root = self.Insert_InOrder_and_PreOrder_Helper(pre, ino)
