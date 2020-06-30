class Stack:
    def __init__(self):
        self.items = []

    def peek(self):
        return self.items[len(self.items) -1]

    def isEmpty(self):
        if self.items:
            return False
        return True


    def push(self, item):
        """Inserts element into stack"""
        self.items.append(item)

    def pop(self):
        removed = self.items.pop()
        return removed

    def size(self):
        return len(self.items)


my_stack = Stack()

print('PUSH')
print(my_stack.push('Dog'))

print('PUSH')
print(my_stack.push('Cat'))

print('PUSH')
print(my_stack.push(True))

print('PUSH')
print(my_stack.push(2387))

print('SHOW:')
print(my_stack.peek())

print('IS EMPTY')
print(my_stack.isEmpty())

print('SIZE')
print(my_stack.size())

print('PEEK')
print(my_stack.peek())

