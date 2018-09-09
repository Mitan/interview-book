from rcviz import callgraph

from TreeNode import TreeNode, print_tree


def create_tree(arr, l, r):
    if l > r or l < 0 or l > len(arr):
        return TreeNode(None)
    if l == r:
        return TreeNode(arr[l])
    middle = (l + r) // 2
    tree = TreeNode(arr[middle])
    tree.left = create_tree(arr, l, middle - 1)
    tree.right = create_tree(arr, middle + 1, r)
    return tree


def create_tree_main(arr):
    length = len(arr)
    return create_tree(arr, 0, length-1)


if __name__ == "__main__":
    vals = [11, 12, 13, 14, 15]
    t = create_tree_main(vals)
    print_tree(t)
    callgraph.render("img/tree.png")
