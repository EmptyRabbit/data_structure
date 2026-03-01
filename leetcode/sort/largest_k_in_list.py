import random



def find_kth_largest(nums, k):
    """
    #215 https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
    数组中的第K大元素
    第K大元素就是第N-K+1大元素(快速选择发）
    参考快排：随机选择一个X，比X小的左边，比X大的右边
    左边个数==K-N返回
    <K-N，去右边递归
    >K-N，去左边递归
    :param nums:
    :param k:
    :return:
    """
    num_length = len(nums)
    if k > num_length:
        return None
    if num_length == 1:
        return nums[0]

    random_key = random.randint(0, num_length - 1)
    compare_key = nums[random_key]
    del nums[random_key]

    left = []
    right = []

    for i in nums:
        if i <= compare_key:
            left.append(i)
        else:
            right.append(i)

    if len(left) == num_length - k:
        return compare_key

    if len(left) > num_length - k:
        diff = len(left) - (num_length - k)
        return find_kth_largest(left, diff)

    if len(left) < num_length - k:
        diff = num_length - k - len(left)
        return find_kth_largest(right, len(right) - diff + 1)


print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
