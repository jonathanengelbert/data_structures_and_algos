
# HASH FORMULA:
# h(item) = item % 2

hash_table = [None] * 11
print(hash_table)

# example of hashing items:
print(54 % 11)
print(77 % 11)

# HASH FUNCTION METHODS:

# The folding method ----

# The folding method for constructing hash functions begins by dividing the item into equal-size pieces
# (the last piece may not be of equal size). These pieces are then added together to give the resulting
# hash value. For example, if our item was the phone number 436-555-4601, we would take the digits and
# divide them into groups of 2 (43,65,55,46,01). After the addition, 43+65+55+46+01, we get 210. If we
# assume our hash table has 11 slots, then we need to perform the extra step of dividing by 11 and keeping
# the remainder. In this case 210 % 11 is 1, so the phone number 436-555-4601 hashes to slot 1. Some folding
# methods go one step further and reverse every other piece before the addition. For the above example, we get
# 43+56+55+64+01=219 which gives 219 % 11=10.


# The mid-square method ----

# Another numerical technique for constructing a hash function is called the mid-square method. We first
# square the item, and then extract some portion of the resulting digits. For example, if the item were 44,
# we would first compute 442=1,936. By extracting the middle two digits, 93, and performing the remainder
# step, we get 5 (93 % 11).

# Dealing with characters ----

# We can also createhash functions for character - based items such as strings.The word “cat” can be thought of
# as a sequence of ordinal values.

ord('c') #  99
ord('a') #  97
ord('t') #  116

# We can then take these three ordinal values, add them up, and use the remainder method to get a hash value:

# 99 + 97 + 116 = 312

# Here is how a function to calculate hashs of a word would work:
print("Here is how a function to calculate hashs of a word would work:" )

def hash_string(s, table_size):
    ord_total = 0
    for l in s:
        ord_total += ord(l)

    print(ord_total % table_size)

hash_string('cat', 11)

# It is interesting to note that when using this hash function, anagrams will always be given the same hash value.
# To remedy this, we could use the position of the character as a weight.

def hash_string_handle_anagram(s, table_size):
    ord_total = 0
    for l in s:
        ord_total += ord(l) * (s.index(l) +1)

    print(ord_total)
    print(ord_total % table_size)

hash_string_handle_anagram('race car', 11)
hash_string_handle_anagram('race car', 11)


# COLISION RESOLUTION

# One method for resolving collisions looks into the hash table and tries to find another open slot to hold
# the item that caused the collision. A simple way to do this is to start at the original hash value position
# and then move in a sequential manner through the slots until we encounter the first slot that is empty. Note
# that we may need to go back to the first slot (circularly) to cover the entire hash table. This collision resolution
# process is referred to as open addressing in that it tries to find the next open slot or address in the hash table.
# By systematically visiting each slot one at a time, we are performing an open addressing technique called linear
# probing.

# Once we have built a hash table using open addressing and linear probing, it is essential that we utilize
# the same methods to search for items.

# An alternative method for handling the collision problem is to allow each slot to hold a reference to a collection
# (or chain) of items. Chaining allows many items to exist at the same location in the hash table. When collisions
# happen, the item is still placed in the proper slot of the hash table. As more and more items hash to the same
# location, the difficulty of searching for the item in the collection increases.

