# Balancing symbols using stacks

from stack_my_implementation import Stack

def are_parentehses_balanced(symbol_string):

    stack = Stack()

    for s in symbol_string:
        print(s)
        if s == '(':
            stack.push(s)
        else:
            if stack.isEmpty():
                return False
            stack.pop()

    if stack.isEmpty():
        return True

    return False

###############################################
# TEST CASES
###############################################

print(are_parentehses_balanced('(()())'))