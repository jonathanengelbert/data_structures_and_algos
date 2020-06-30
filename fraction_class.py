def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def show(self):
        print(self.top, "/", self.bottom)

        return self

    def __str__(self):
        return str(self.top) + "/" + str(self.bottom)

    def __add__(self, other_factor):
        new_top = self.top * other_factor.bottom + self.bottom * other_factor.top
        new_bottom = self.bottom * other_factor.bottom
        common = gcd(new_top, new_bottom)
        return Fraction(new_top // common, new_bottom // common)

    def __eq__(self, other):
        first = self.top * other.bottom
        second = other.top * self.bottom
        return first == second

    def getNum(self):
        return self.top


    def getDen(self):
        return self.bottom


f1 = Fraction(1,4)
f2 = Fraction(2,4)

print(f1.getDen())

