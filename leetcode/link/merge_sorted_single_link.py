from .utils import LinkNode


def merge_sorted_single_link(l1, l2):
    """
    #21 合并两个有序单链表
    1->2->4
    1->3->4
    结果为 1->1->2->3->4
    """
    head = LinkNode(None)
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

