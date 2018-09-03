from LinkedList_2 import Node, generate_test_list


def insert_before(l, value):
    node = Node(value)
    node.next = l
    return node


def align(l, shift):
    for _ in range(shift):
        l = insert_before(l, 0)
    return l


def length(l):
    length = 0
    while l:
        length += 1
        l = l.next
    return length


def sum_numbers(l1, l2):
    len1 = length(l1)
    len2 = length(l2)
    diff = len1 - len2
    if diff > 0:
        l2 = align(l2, diff)
    else:
        l1 = align(l1, -diff)
    sum_helper, carry = sum_number_helper(l1, l2)
    if carry:
        sum_helper = insert_before(sum_helper, carry)
    return sum_helper


def sum_number_helper(l1, l2):
    if not l1 and not l2:
        return None, 0
    next_sum, carry = sum_number_helper(l1.next, l2.next)
    current_digit = l1.data + l2.data + carry
    current_node = insert_before(next_sum, current_digit % 10)
    return current_node, current_digit // 10


if __name__ == "__main__":
    l1 = [9,9, 9]
    l2 = [1]

    l1 = generate_test_list(l1)
    l2 = generate_test_list(l2)

    new_l = sum_numbers(l1, l2)
    new_l.print_list()