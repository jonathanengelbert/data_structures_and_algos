# WORKS BETTER BECAUSE IT ITERATES OVER THE 26 LETTERS OF THE ALPHABET LAST
# THEREFORE, ANY (N) BEYOND 26 WILL BE THE SAME

import string
from timeit import Timer
def anagram_my_solution_count_compare(s1, s2):
    matches = True

    d1 = dict.fromkeys(string.ascii_lowercase, 0)
    d2 = dict.fromkeys(string.ascii_lowercase, 0)

    for l in s1:
        d1[l] +=1

    for l in s2:
        d2[l] +=1

    # compare dictionaries
    for l, count in d1.items():
        if d2[l] != count:
            matches = False
            return matches

    return matches

def test1():
    anagram_my_solution_count_compare('apple','pleapp')

    def test1():
        anagram_my_solution_count_compare('applealKJSdklojasKLdjaslkjdlksajdlkasjssdsadsadsadsadsadsadsadsadsadsadsadsadasdsadsadsadsadsadsadsadasdasdasdasdasdsadasdasdasdsadsadsadsadasdasdsadklsajdklsajdkljsalkdjlsakjdlksajdlkasjdlksajdlksajdlkasjldjsaljdk','pleapasdsadsadkjsadkjhaskjdhsakjhdkjsahdkjhaskjldklajhsdkljashdkjsajkdhsakjldhlkjsahdjkashdkjasdsadsadsadsadasdsadasdsadsadasdsadasdsadsadsadasdsadsadsadsadasdasdasdsadasdasasdsadashaskjdhsa')

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")

