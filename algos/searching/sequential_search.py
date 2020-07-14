
# A simple sequential search implementation
def sequential_search(l, search_item):
    position = 0

    for i in l:
        if i == search_item:
            return position
        position += 1

    return 'Not Found'

print(sequential_search([1, 5, 7, 8, 23, 4543], 1))

# A sequential search taking advantage of a sorted list
def sequential_ordered_search(l, search_item):
    position = 0

    for i in l:
        if i > search_item:
            return 'Not Found'
        if i == search_item:
            return position
        position += 1

    return 'Not Found'

print(sequential_ordered_search([1, 5, 7, 8, 23, 45430], 6))
