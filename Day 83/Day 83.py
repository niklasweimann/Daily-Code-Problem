from Tree import Tree, Node


class invertTree(Tree):
    def invert(self):
        self.invertTree(self.root)

    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(
                root.right), self.invertTree(root.left)
        return root


t = invertTree()
t.Insert("f")
t.Insert("d")
t.Insert("b")
t.Insert("g")
print("Before:")
t.Display()
t.invert()
print("After:")
t.Display()
