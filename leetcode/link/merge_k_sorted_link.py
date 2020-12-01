class LinkNode():
    def __init__(self, val, _next):
        self.val = val
        self.next_node = _next

    def to_list(self):
        result = []
        _next_node = self
        while _next_node:
            result.append(_next_node.val)
            _next_node = _next_node.next_node
        return result


def merge_k_link(link_list):
    """
    #23
    分治实现
    1、只有一个链表时返回该链表
    2、只有两个链表时返回合并后的链表
    3、有两个以上链表时，拆分成两部分分别合并
    :param link_list:
    :return:
    """

    def merge_two_list(l1, l2):
        head = LinkNode(None, None)
        p = head  # 保存头结点执行，最后输出head头节点

        while l1 and l2:
            if l1.val <= l2.val:
                p.next_node = l1
                l1 = l1.next_node
            else:
                p.next_node = l2
                l2 = l2.next_node

            p = p.next_node

        if l1:
            p.next_node = l1
        else:
            p.next_node = l2

        return head.next_node

    def merge(l_list, start, end):
        if start == end:
            return l_list[start]

        mid = int((start + end) / 2)
        left = merge(l_list, start, mid)
        right = merge(l_list, mid + 1, end)

        return merge_two_list(left, right)

    n = len(link_list)
    if n == 0:
        return None
    return merge(link_list, 0, n - 1)

if __name__=='__main__':
    result = []
    result.append(None)
    two = LinkNode(1, None)
    two.next_node = LinkNode(2, None)
    result.append(two)
    result.append(None)

    three = LinkNode(3, None)
    three.next_node = LinkNode(4, None)
    result.append(three)

    a = merge_k_link(result)
    b = a.to_list()
    print(b)
