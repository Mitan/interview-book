from LinkedList_2 import *
"""
class Cat:
    def __init__(self):
        pass


class Dog:
    def __init__(self):
        pass
"""


class AnimalWrapper:
    def __init__(self, animal, time):
        self.time = time
        self.animal = animal

class ListHeadTail:
    def __init__(self):
        self.head = None
        self.tail = None

class ShelterQueue:
    def __init__(self):
        self.time = 0
        # dog, cat
        self.queue = [ListHeadTail(), ListHeadTail()]

    def enqueue(self, animal):
        if animal[0] == 'c':
            self.__enqueue(animal, 1, self.time)
        elif animal[0] == 'd':
            self.__enqueue(animal, 0, self.time)
        else:
            raise Exception("wrong animal")
        self.time += 1

    def __enqueue(self, animal,cat_dog_index, time):
        wrapper = Node(AnimalWrapper(animal, time))

        if not self.queue[cat_dog_index].head:
            self.queue[cat_dog_index].head = wrapper
            self.queue[cat_dog_index].tail = wrapper
        else:
            self.queue[cat_dog_index].tail.next = wrapper
            self.queue[cat_dog_index].tail = wrapper

    def dequeueAny(self):
        if not (self.queue[0].head or self.queue[1].head):
            raise Exception("queue empty")
        time = float('inf')
        isCat = False
        if self.queue[0].head and self.queue[0].head.data.time < time:
                time = self.queue[0].head.data.time
                isCat = False
        if self.queue[1].head and self.queue[1].head.data.time < time:
                time = self.queue[1].head.data.time
                isCat = True
        if isCat:
                return self.dequeueCat()
        else:
                return self.dequeueDog()

    def dequeueCat(self):
            return self.__dequeue(1)

    def dequeueDog(self):
            return self.__dequeue(0)

    def __dequeue(self, cat_dog_index):
            if not self.queue[cat_dog_index].head:
                raise Exception("can’t dequeue - empty")
            animal = self.queue[cat_dog_index].head.data.animal
            self.queue[cat_dog_index].head = self.queue[cat_dog_index].head.next
            if not self.queue[cat_dog_index].head:
                self.queue[cat_dog_index].tail = None
            return animal


if __name__ == "__main__":
    queue = ShelterQueue()
    vals = ["c1", "d1", "d2", "c2", "c3"]
    for v in vals:
        queue.enqueue(v)
    print(queue.dequeueCat())
    print(queue.dequeueDog())
    print(queue.dequeueAny())
    queue.enqueue("d3")
    print(queue.dequeueDog())

