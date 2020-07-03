import time

numbers = [23 , 1999, -23333, 1, 0, 675, 90]

def find_minimum_fast(nums):
    """
    Finds the minimum number in a list
    O(n2)
    :param nums:
    :return:
    """
    smallest = nums[0]
    for n in nums:
        if n < smallest:
            smallest = n

    return smallest

def find_minimum_slow(nums):
    """
    Finds the minimum number in a list
    O(n)
    :param nums:
    :return:
    """

    smallest = nums[0]
    issmallest = True
    for i in nums:
        issmallest = True
        # print(i)
        for j in nums:
            # print(i, j)
            if i > j:
                issmallest = False
        if issmallest:
            smallest = i


    return(smallest)

start1 = time.time()
find_minimum_slow(numbers)
end1 = time.time()
print("SLOW: ", end1 -  start1)

# find_minimum_fast(numbers)
# start2 = time.time()
# end2 = time.time()
# print("FAST: ", end2 -  start2)
