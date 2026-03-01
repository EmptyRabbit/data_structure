import random


def quick_sort(nums):
    """
    #912 快速排序：https://leetcode-cn.com/problems/sort-an-array/
    :param nums:
    :return:
    """
    if len(nums) <= 1:
        return nums

    random_num = random.randint(0, len(nums) - 1)
    compare = nums[random_num]
    del nums[random_num]

    left = []
    right = []

    for i in nums:
        if i < compare:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [compare] + quick_sort(right)


print(quick_sort([4, 1]))
