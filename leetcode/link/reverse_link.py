"""
链表反转
思路：原来指向后一个节点，现改为指向前一个节点，再变更头节点（原头节点指向尾节点后置null）
1、保存当前节点的next节点
2、当前next指向当前的前一个
3、变更当前节点为next
图解：https://blog.csdn.net/xyh269/article/details/70238501
"""


def reverse_single_link(head):
    """
    #206
    :param head:
    :return:
    """
    pre_node = None
    while head:
        tmp = head.next_node
        head.next_node = pre_node  # head next指向前一个
        pre_node = head  # 下一个pre_node指向当前的head，此时head next已指向前一个

        head = tmp

    return pre_node


def reverse_single_link_test(head):
    if not head or not head.next_node:
        return

    new_head = reverse_single_link(head.next_node)
    head.next_node.next_node = head
    head.next_node = None
    return new_head



