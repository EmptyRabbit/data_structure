def merge(mlist, m, nlist, n):
    """
    #88
    todo 查看其他指针移动的思路
    :param mlist:
    :param m:
    :param nlist:
    :param n:
    :return:
    """
    if n > 0:
        mlist[-n:] = mlist
    mlist.sort()
