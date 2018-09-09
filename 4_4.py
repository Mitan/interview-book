from rcviz import callgraph

from TreeNode import TreeNode, print_tree


def check_balance(tree):
    if not tree:
        return True, 0
    left_ans, left_height = check_balance(tree.left)
    if not left_ans:
        return False, -1
    right_ans, right_height = check_balance(tree.right)
    if not right_ans:
        return False, -1
    return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1


def check_balance_tree_main(root):
    return check_balance(root)[0]


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
    fail_node = TreeNode(-100)
    l2.right = fail_node
    print_tree(root)
    callgraph.render("img/tree.png")
    print(check_balance_tree_main(root))
