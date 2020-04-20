import copy


def insertion_sort(nums):
    """
    #912 插入排序：https://leetcode-cn.com/problems/sort-an-array/
    :param nums:
    :return:
    """
    sorted_key = 0

    while sorted_key + 1 < len(nums):
        sorted_key += 1
        for i in range(sorted_key + 1):
            unsorted = copy.copy(nums[sorted_key])
            if unsorted <= nums[i]:
                del nums[sorted_key]
                nums.insert(i, unsorted)
                break

    return nums


print(insertion_sort([2, 1]))
