def fib(n):
    """
    #509
    :param n:
    :return:
    """
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


def factorial(n):
    """
    n!
    :param n:
    :return:
    """
    if n == 1:
        return 1
    return factorial(n - 1) * n


def permute(nums_list):
    """
    #46
    给定一个没有重复数字的序列，返回其所有可能的全排列。
    递归：元素为n，对n-1的每个结果插入第n个的情况
    :param nums_list:
    :return:
    """
    length = len(nums_list)
    if length == 1:
        return [nums_list]

    last = permute(nums_list[:-1])

    result = []
    for l in last:
        for i in range(len(l) + 1):
            tmp = l[:]
            tmp.insert(i, nums_list[-1])
            result.append(tmp)

    return result


permute([1, 2, 3])
