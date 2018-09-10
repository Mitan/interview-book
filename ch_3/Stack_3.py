from LinkedList_2 import Node


class MyStack:
    def __init__(self):
        self.top = None

    def push(self, v):
        node = Node(v)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            raise Exception("stack is empty")
        v = self.top.data
        self.top = self.top.next
        return v

    def peek(self):
        if not self.top:
            raise Exception("stack is empty")
        return self.top.data

    def is_empty(self):
        return self.top is None


if __name__ == "__main__":
    s = MyStack()
    print(s.is_empty())
    s.push(1)
    print(s.peek())
    print(s.pop())
    print(s.is_empty())