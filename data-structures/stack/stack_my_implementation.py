class Stack:
    def __init__(self):
        self.items = []

    def show(self):
        return self.items

    def peek(self):
        if not self.items:
            return 0
        return self.items[len(self.items) -1]

    def isEmpty(self):
        if self.items:
            return False
        return True

    def push(self, item):
        """Inserts element into stack"""
        self.items.append(item)

    def pop(self):
         return self.items.pop()

    def size(self):
        return len(self.items)


# my_stack = Stack()
#
# print('PUSH')
# print(my_stack.push('Dog'))
#
# print('PUSH')
# print(my_stack.push('Cat'))
#
# print('PUSH')
# print(my_stack.push(True))
#
# print('PUSH')
# print(my_stack.push(2387))
#
# print('SHOW:')
# print(my_stack.peek())
#
# print('IS EMPTY')
# print(my_stack.isEmpty())
#
# print('SIZE')
# print(my_stack.size())
#
# print('PEEK')
# print(my_stack.peek())
#
# ###########################################################################################
# # Write a function revstring(mystr) that uses a stack to reverse the characters in a string.
# ###########################################################################################
#
# def rev_string(s):
#     stack = []
#     s_list = list(s)
#     while len(s_list) > 0:
#         stack += s_list.pop()
#     print(stack)
#
def rev_string(s):
    my_stack = Stack()
    i = len(s)
    for l in s:
        my_stack.push((s[i - 1]))
        i -= 1
    return my_stack.show()

#
# print(rev_string('This is my String'))

