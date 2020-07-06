
def convert(n, base):
    lookup = '0123456789ABCDEF'

    if n < base:
        return lookup[n]

    return convert(n // base, base) + lookup[n % base]

print(convert(1453, 16))
print(convert(10, 2))


