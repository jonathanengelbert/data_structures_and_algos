class Queue:
    def __init__(self):
        self.items = []

    def describe(self):
        return self.items

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
        return

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



# my_queue = Queue()
# print(my_queue.enqueue('Dog'))
# print(my_queue.enqueue('Cat'))
# print(my_queue.enqueue(True))
# print(my_queue.size())
# print(my_queue.describe())
# print(my_queue.dequeue())
# print(my_queue.describe())
# print(my_queue.size())
