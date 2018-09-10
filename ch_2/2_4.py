from LinkedList_2 import *


def reorder(my_list, x):
    if not my_list or not my_list.next:
        return my_list
    head = my_list
    n = my_list
    while n and n.next:
        while n.next and  n.next.data < x:

            new_head = Node(n.next.data)
            new_head.next = head
            head = new_head
            n.next = n.next.next

        n = n.next
    return head



if __name__ == "__main__":
    """
    vals = [0,7,2,5, 8,3,1]
    l = generate_test_list(vals)

    x = 5
    new_l = reorder(l, x)
    new_l.print_list()
    """
    a = [1,2]
    b = a
    c = a.copy()
    print(a,b,c)
    a.append(3)
    print(a,b,c)