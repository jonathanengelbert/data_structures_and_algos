stringOne = 'earth'
stringTwo = 'heart'

def anagram_solution_sort_compare(s1, s2):
    matches = True
    if len(s1) != len(s2):
        matches = False
        return print(matches)

    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0

    while pos < len(s1):
        print(pos)
        if alist1[pos] != alist2[pos]:
            matches = False
            return print(matches)
        pos += 1

    print(matches)

anagram_solution_sort_compare(stringOne, stringTwo)

