from node import Node

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def show_all_nodes(self):
        if self.is_empty():
            return("NO NODES IN LIST")

        current = self.head

        while current:
            print(current.get_data())
            current = current.get_next()
        return "End of nodes"

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    # LINKED LIST TRAVERSAL TECHNIQUES
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        while current:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()

        return False

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

    # O(n) version of append

    def append(self, item):
        if self.search(item):
            return 'Item already in list'

        current = self.head
        while current:
            if not current.get_next():
                return current.set_next(Node(item))

            current = current.get_next()





my_list = UnorderedList()
my_list.add('Dog')
my_list.add('Cat')
my_list.add('Mouse')
my_list.append('Dogs')
my_list.append('Monkey')
my_list.add('Stuff')
print(my_list.show_all_nodes())
