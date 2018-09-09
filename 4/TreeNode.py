from rcviz import viz, callgraph


class TreeNode:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

@viz
def print_tree(tree):
        if tree.left:
            print_tree(tree.left)
        print(tree.data)
        if tree.right:
            print_tree(tree.right)
        return tree.data


if __name__ == "__main__":
    root = TreeNode(2)
    l1 = TreeNode(0)
    l0 = TreeNode(-1)
    l2 = TreeNode(1)
    r1 = TreeNode(5)

    l1.left = l0
    l1.right = l2

    root.left = l1
    root.right = r1

    print_tree(root)
    callgraph.render("tree.png")
