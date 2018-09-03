from LinkedList_2 import generate_test_list


def remove_duplicates(my_list):
    previous = None
    data_dict = set()
    n = my_list
    while n:
        if n.data in data_dict:
            previous.next = n.next
        else:
            data_dict.add(n.data)
            previous = n
        n = n.next
    return my_list


def remove_duplicates_no_buffer(my_list):
    first = my_list
    while first:
        previous = first
        second = first.next
        while second:
            if second.data == first.data:
                previous.next = second.next
            else:
                previous = second
            second = second.next
        first = first.next
    return my_list


if __name__ == "__main__":
    vals = [0,1,2, 3,2,4, 0,0]
    l = generate_test_list(vals)
    l_1 = generate_test_list(vals)

    remove_duplicates(l)
    remove_duplicates_no_buffer(l_1)
    l.print_list()
    l_1.print_list()
