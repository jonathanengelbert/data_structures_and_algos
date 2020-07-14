# Write a recursive function to compute the factorial of a number.

def factorial_recursevely(n):
    if n == 1:
        return n

    return n * factorial_recursevely(n - 1)

print(factorial_recursevely(21))

# Write a recursive function to reverse a list.

def reverse_list(l):
    if len(l) == 1: 
        return l

    return reverse_list(l[1:]) + l[:1]

print(reverse_list([2, 5, 7, 9, 123]))
