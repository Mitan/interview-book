from ch_4.TreeNode import TreeNode


def print_arrays(tree):
    if not tree:
        return None
    if not tree.left and not tree.right:
        return [[tree.data]]
    left = print_arrays(tree.left)
    right = print_arrays(tree.right)
    child_arrays = merge_array_lists(left, right)
    return [[tree.data] + x for x in child_arrays]


def merge_array_lists(arr_list_1, arr_list_2):
    if not arr_list_1:
        return arr_list_2
    if not arr_list_2:
        return arr_list_1
    ans = []
    for arr1 in arr_list_1:
        for arr2 in arr_list_2:
            ans = ans + merge_two_arrays(arr1, arr2)
    return ans


def merge_two_arrays(a1, a2):
    if not a1:
        return [a2]
    if not a2:
        return [a1]

    return [[a1[0]] + x for x in merge_two_arrays(a1[1:], a2)] \
                  + [[a2[0]] + x for x in merge_two_arrays(a1, a2[1:])]


if __name__ == "__main__":
    root = TreeNode(2)
    l1 = TreeNode(1)
    l0 = TreeNode(0)
    l2 = TreeNode(3)
    l22 = TreeNode(-1)

    l0.right = l1
    l0.left = l22
    root.right = l2
    root.left = l0
    print(print_arrays(root))