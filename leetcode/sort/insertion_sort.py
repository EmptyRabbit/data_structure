import copy


def insertion_sort(nums):
    """
    #todo 超过时间
    #912 插入排序：https://leetcode-cn.com/problems/sort-an-array/
    分为已排序和未排序，每次从未排序中选第一个，插入到已排序中合适的位置
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
