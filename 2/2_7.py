from LinkedList_2 import generate_test_list, Node


def check_length(l):
    length = 1
    while l.next:
        length += 1
        l = l.next
    return l, length


def find_first_intersect(longer, shorter, diff):
    for i in range(diff):
        longer = longer.next

    i = 0
    while longer != shorter and longer:
        longer = longer.next
        shorter = shorter.next
        i += 1

    if not longer:
        raise Exception
    return i


def check_intersect(list1, list2):
    node1, l1 = check_length(list1)
    node2, l2 = check_length(list2)
    if node1 != node2:
        return False, None
    diff = l1 - l2
    if diff > 0:
        i = find_first_intersect(list1, list2, diff)
        ans = (i + diff, i)
    else:
        i = find_first_intersect(list2, list1, -diff)
        ans = (i, i - diff)
    return True, ans


if __name__ == "__main__":
    vals = [0,7,2,5, 8,3,1]
    n1 = Node(3)
    n2 = Node(4)
    n1.next = n2

    n3 = Node(2)
    n3.next = n1
    n4 = Node(1)
    n4.next = n3

    n5 = Node(2)
    n5.next = n1

    print(check_intersect(n1, n5))







