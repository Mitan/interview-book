from Stack_3 import MyStack


class MyQueue:
    def __init__(self):
        self.back = MyStack()
        self.front = MyStack()

    def add(self, item):
        self.back.push(item)

    def move_back_stack(self):
        while not self.back.is_empty():
            v = self.back.pop()
            self.front.push(v)

    def remove(self):
        if self.is_empty():
            raise Exception("queue is empty")
        if self.front.is_empty():
            self.move_back_stack()
        return self.front.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("queue empty")
        if self.front.is_empty():
            self.move_back_stack()
        return self.front.peek()

    def is_empty(self):
        return self.back.is_empty() and self.front.is_empty()


if __name__ == "__main__":
        q = MyQueue()
        q.add(11)
        q.add(2)
        print(q.peek())
        print(q.remove())
        print(q.remove())
        print(q.peek())

