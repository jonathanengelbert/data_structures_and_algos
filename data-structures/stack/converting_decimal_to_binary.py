# The Divide by 2 algorithm assumes that we start with an integer greater than 0. A simple iteration then
# continually divides the decimal number by 2 and keeps track of the remainder. The first division by 2 gives
# information as to whether the value is even or odd. An even value will have a remainder of 0.
# It will have the digit 0 in the ones place. An odd value will have a remainder of 1 and will have the
# digit 1 in the ones place. We think about building our binary number as a sequence of digits; the first
# remainder we compute will actually be the last digit in the sequence

from stack_my_implementation import Stack

def convert_decimal_to_binary(num):
    remainder = num
    stack = Stack()

    if remainder % 2 == 0:
        stack.push(0)
    else:
        stack.push(1)

    while remainder > 1:
        remainder //= 2
        if remainder % 2 == 0:
            stack.push(0)
        else:
            stack.push(1)

    binary_number = ''
    while not stack.isEmpty():
        binary_number += str(stack.pop())

    return int(binary_number)


# runestone implementation (more sophisticated, shorter, not sure about performance
def divideBy2(decNumber):
   remstack = Stack()

   while decNumber > 0:
       rem = decNumber % 2
       remstack.push(rem)
       decNumber = decNumber // 2

   bin_string = ''
   while not remstack.isEmpty():
       bin_string += str(remstack.pop())

   return bin_string

# MY IMPROVED VERSION OF IT. ACCOUNTS FOR 0

from stack_my_implementation import Stack


def convert_decimal_to_binary_revised(num):
    remStack = Stack()

    while num > 0:
        remStack.push(num % 2)
        num //= 2

    binaryString = ''
    while not remStack.isEmpty():
        binaryString += str(remStack.pop())

    return binaryString or 0



###############################################
# TEST CASES
###############################################

print(convert_decimal_to_binary(1000))
print(divideBy2(1000))
print(convert_decimal_to_binary_revised(1000))
