from .utils import LinkNode


def merge_sorted_single_link(head_a, head_b):
    """
    #21 合并两个有序单链表
    1->2->4
    1->3->4
    结果为 1->1->2->3->4
    ----------------------
    比较两个节点大小，如果相等，返回a->b，然后b的next指向a，b两个next节点返回的链表，递归
    :param head_a:
    :param head_b:
    :return:
    """
    if not head_b:
        return head_a
    if not head_a:
        return head_b

    if head_a.val == head_b.val:
        node = LinkNode(head_a.val, head_b)
        head_b.next_node = merge_sorted_single_link(head_a.next_node, head_b.next_node)
    elif head_a.val < head_b.val:
        node = LinkNode(head_a.val)
        node.next_node = merge_sorted_single_link(head_a.next_node, head_b)
    else:
        node = LinkNode(head_b.val)
        node.next_node = merge_sorted_single_link(head_a, head_b.next_node)

    return node
