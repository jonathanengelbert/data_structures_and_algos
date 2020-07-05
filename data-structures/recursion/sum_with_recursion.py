nums = [1, 3, 5, 7, 9]

def add(nums):
    if len(nums) == 1:
        return nums[0]

    return nums[0] + add(nums[1:])

print(add(nums))
