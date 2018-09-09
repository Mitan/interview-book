class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

    def print_list(self):
        ans = []
        current = self
        while current:
            ans.append(current.data)
            current = current.next
        print(ans)






def generate_test_list(val_list):
    if not val_list:
        return None
    reverse_list = list(reversed(val_list))
    head = Node(reverse_list[0])

    for i in range(1, len(reverse_list)):
        new_head = Node(reverse_list[i])
        new_head.next = head
        head = new_head
    return head


if __name__ == "__main__":
    vals = [1,2,3,4]
    l = generate_test_list(vals)
    l.print_list()