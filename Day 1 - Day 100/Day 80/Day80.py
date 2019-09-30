from Tree import Tree


class deepTree(Tree):
    def find(self, root, level, maxLevel, res):
        if root is None:
            return
        level += 1
        self.find(root.left, level, maxLevel, res)
        if level > maxLevel[0]:
            res[0] = root
            maxLevel[0] = level
        self.find(root.right, level, maxLevel, res)

    def get_deepest_node(self):
        res = [-1]
        maxLevel = [-1]
        self.find(self.root, 0, maxLevel, res)
        return res[0]


t = deepTree()
t.Insert("f")
t.Insert("d")
t.Insert("b")
t.Insert("g")
print(t.Display())
print(t.get_deepest_node())
