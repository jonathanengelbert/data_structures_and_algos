from timeit import Timer

stringOne = 'earth'
stringTwo = 'heart'

def anagram_solution_checking_off(s1, s2):
    stillOk = True
    if len(s1) != len(s2):
        stillOk = False

    alist = list(s2)
    pos1 = 0

    while pos1 < len(s1) and stillOk:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOk = False

        pos1 = pos1 + 1

    return stillOk

anagram_solution_checking_off(stringOne, stringTwo)
def test1():
    anagram_solution_checking_off('apple','pleap')

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")

