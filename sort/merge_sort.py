def merge_sort(nums, start, end):
    """
    #912 归并排序：https://leetcode-cn.com/problems/sort-an-array/
    5 4 7 9 3 8 2 1
    5 4 7 9 | 3 8 2 1
    5 4 | 7 9  |  3 8 | 2 1
    5 | 4  |  7 | 9    |    3 | 8  |  2 | 1

    4 5 | 7 | 9  |  3 | 8  |  2 | 1
    4 5 7 9 | 3 | 8  |  2 | 1
    4 5 7 9 | 3 8 | 2 | 1
    4 5 7 9 | 3 8 | 1 2
    4 5 7 9 | 1 2 3 8
    1 2 3 4 5 7 8 9
    :param nums:
    :param start:
    :param end:
    :return:
    """

    def merge(array, start, mid, end):
        left = array[start:mid]
        right = array[mid:end]
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):  # 左右游标都在数组可取值范围内，有任意一个不在，即结束 or 将剩下的移动
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        if i == len(left):  # left的部分已全部收集
            result.extend(right[j:])
        if j == len(right):  # right的部分已全部收集
            result.extend(left[i:])

        array[start:end] = result[:]

    if len(nums[start:end]) <= 1:  # 直到左边/右边个数=1，退出
        return nums[start:end]

    mid = int((start + end + 1) / 2)  # 取中间值
    merge_sort(nums, start, mid)  # 左边的部按归并排好序
    merge_sort(nums, mid, end)  # 右边的部分按归并排好虚
    merge(nums, start, mid, end)  # 合并两个有序序列


nums = [4, 3, 2, 1, 0]
merge_sort(nums, 0, 5)
print(nums)
