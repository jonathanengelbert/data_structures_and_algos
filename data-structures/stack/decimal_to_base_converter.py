from stack_my_implementation import Stack

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
        print(newString)

    return newString

# print(baseConverter(25,2))
# print(baseConverter(25,16))
print(baseConverter(26, 26))