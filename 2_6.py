from LinkedList_2 import Node, generate_test_list


def reverse_list(my_list):
    length = 0
    head = None
    while my_list:
        length += 1
        new_head = Node(my_list.data)
        new_head.next = head
        head = new_head
        my_list = my_list.next
    return head, length


def check_palindrom(my_list):
    if not my_list:
        return True
    reversed, length = reverse_list(my_list)
    for _ in range(length // 2):
        if reversed.data != my_list.data:
            return False
        my_list = my_list.next
        reversed = reversed.next
    return True


def check_palindrom2(my_list):
    if not my_list or not my_list.next:
        return True
    p1 = my_list
    p2 = my_list.next
    length = 1
    # half length
    first_half = [p1.data]
    while p2.next and p2.next.next:
        p1 = p1.next
        p2 = p2.next.next
        first_half.append(p1.data)
        length += 1
    if p2.next:
        p1 = p1.next.next
    else:
        p1 = p1.next
    for i in range(length):
        if first_half[-1-i] != p1.data:
            return False
        p1 = p1.next
    return True


if __name__ == "__main__":
    vals = [0, 7, 2, 5, 8, 3, 1]
    vals = [0, 7, 5,7, 0]
    l = generate_test_list(vals)

    print(check_palindrom2(l))
