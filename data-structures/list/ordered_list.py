from node import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()

        def remove(self, item):
            # list is empty, quit
            if self.is_empty():
                return 'The list is currently empty'

            current = self.head
            previous = None

            while current:
                if current.get_data() == item:
                    if previous:
                        previous.set_next(current.get_next())
                    else:
                        self.head = current.get_next()

                previous = current
                current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        while current:
            if current.get_data() == item:
                return True

            if current.get_data() > item:
                return

            else:
                current = current.get_next()

        return False


    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)


mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
