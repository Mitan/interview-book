from LinkedList_2 import generate_test_list, Node


def find_k_last(my_list, k):
    p2 = my_list
    for i in range(k):
        if not p2:
            raise Exception()
        p2 = p2.next
    p1 = my_list
    while p2:
        p2 = p2.next
        p1 = p1.next
    return p1


def find_k_last_recursive(head, k):
    global node
    if not head:
        return 0
    else:
        lvl = find_k_last_recursive(head.next, k) + 1
        if lvl == k:
            node = head
        return lvl

if __name__ == "__main__":
    vals = [0, 1, 2, 3, 4]
    l = generate_test_list(vals)
    """
    k = 2
    # node = find_k_last(l,k)
    node = Node(None)
    length = find_k_last_recursive(l, k)
    if length < k:
        raise Exception("node is %d" % (length))
    print(node.data)
    """

