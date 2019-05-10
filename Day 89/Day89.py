from Tree import Tree, Node


class valid_tree(Tree):
    def isValid(self, root, l=None, r=None):
        if not root:
            return True

        if l and root.value < l.value:
            return False

        if r and root.value > r.value:
            return False

        return self.isValid(root.left, l, root) and self.isValid(root.right, root, r)


t = valid_tree()
t.Insert("f")
t.Insert("d")
t.Insert("b")
t.Insert("g")
t.Display()
print(t.isValid(t.root))
