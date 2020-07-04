# When a closing symbol does appear, the only difference is that we must check to be sure that
# it correctly matches the type of the opening symbol on top of the stack. If the two symbols
# do not match, the string is not balanced. If the entire string is processed
# and nothing is left on the stack, the string is correctly balanced.

# This dependency is simply a stack
from stack_my_implementation import Stack

def matches(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)

def are_symbols_balanced(symbols):

    stack = Stack()
    index = 0
    for s in symbols:
        if s in '([{':
            stack.push(s)
        else:
            if stack.isEmpty():
                return False
            else:
                # print(index, stack.show(), "\n")
                top = stack.pop()
                # print(index, stack.show(), "\n")
                if not matches(top, s):
                    return False
        index += 1

    if stack.isEmpty():
        return True

    return False

###############################################
# TEST CASES
###############################################

# print(are_symbols_balanced('{({([][])}())}'))
print(are_symbols_balanced('[({}))]'))
