import math


# DIVIDE AND CONQUER ALGO
def binary_search(l, search_item):
    midpoint = math.floor(len(l) / 2)
    found = False

    while not found and midpoint > 0 and midpoint < len(l):

        if l[midpoint] == search_item:
            found = True
            return midpoint
        if search_item < l[midpoint]:
            midpoint -= 1

        else:
            midpoint += 1



    return 'Not Found'

print(binary_search([1, 2, 3, 4, 5, 6, 7, 9, 9, 10], 3))

# DIVIDE AND CONQUER ALGO (RECURSIVE VERSION)
def binary_search(l, search_item):
    if len(l) == 0:
        return False

    print(l)
    midpoint = len(l) // 2

    if l[midpoint ] == search_item:
        return True

    if search_item < l[midpoint]:
        return binary_search(l[:midpoint], search_item)
    else:
        return binary_search(l[midpoint + 1:], search_item)


print(binary_search([-23, 1, 2, 3, 4, 5, 6, 7, 9, 9, 10], 9))
print(binary_search([3, 5, 6, 8, 11, 12, 14, 15, 17, 18], 8))