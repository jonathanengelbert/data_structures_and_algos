from deque import Deque

def is_palindrome(string):
    reversed = Deque()

    for l in string:
        reversed.add_rear(l)

    while reversed.size() > 1:
        first = reversed.remove_front()
        second = reversed.remove_rear()
        if first != second:
            return False

    return True

print(is_palindrome('racecar'))
print(is_palindrome('banana'))
print(is_palindrome('radar'))
print(is_palindrome('adasdfsafafdsaf'))
print(is_palindrome('mom'))

