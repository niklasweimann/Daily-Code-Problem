from Tree import Tree


class AdTree(Tree):
    def calculate_Tree(self):
        return self.calculate_Tree_Helper(self.root)

    def calculate_Tree_Helper(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return int(node.value)

        left_sum = self.calculate_Tree_Helper(node.left)
        right_sum = self.calculate_Tree_Helper(node.right)

        if node.value == '+':
            return left_sum + right_sum
        elif node.value == '-':
            return left_sum - right_sum
        elif node.value == '*':
            return left_sum * right_sum
        elif node.value == '/':
            return left_sum / right_sum
        else:
            raise Exception()


# Tast code
tree = AdTree()
in_order = ['5', '*', '4', '+', '100', '-', '20']
pre_order = ['+', '*', '5', '4', '-', '100', '20']
tree.Insert_InOrder_and_PreOrder(pre_order, in_order)
tree.Display()
print(tree.calculate_Tree())
