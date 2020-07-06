
def reverse_with_recursion(s):
    if len(s) == 0:
        return s
    if s and len(s) == 1:
        return s[0]

    return reverse_with_recursion(s[1:]) + s[0]

print(reverse_with_recursion("hello"))
print(reverse_with_recursion("l"))
print(reverse_with_recursion("follow"))
print(reverse_with_recursion(""))
