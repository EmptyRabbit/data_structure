import copy


def selection_sort(nums):
    """
    #todo 超过时间
    #912 选择排序：https://leetcode-cn.com/problems/sort-an-array/
    :param nums:
    :return:
    """
    append_key = 0
    while append_key < len(nums) - 1:
        min = append_key
        for i in range(len(nums[append_key:]) - 1):
            if nums[append_key + i + 1] < nums[min]:
                min = append_key + i + 1

        tmp = copy.copy(nums[min])
        del nums[min]
        nums.insert(append_key, tmp)
        append_key += 1

    return nums


print(selection_sort([1,2,6,5,4]))
