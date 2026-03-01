"""
todo 待优化时间和空间复杂度
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'val:{self.val}, (l:{self.left}, r:{self.right})'

    def __repr__(self):
        return f'val:{self.val}, (l:{self.left}, r:{self.right})'


def load_list_to_binary_tree(tree_list, cursor=1):
    """
    从数组 [1,2,3,4,5] 还原二叉树
    取第一个为根节点，分为左右两个子树，递归转左右两个子树
    :param tree_list:
    :return:
    """
    if not tree_list or cursor > len(tree_list):
        return None

    tree_node = TreeNode(tree_list[cursor - 1])
    tree_node.left = load_list_to_binary_tree(tree_list, cursor * 2)  # 若游标超出len，代表left为空
    tree_node.right = load_list_to_binary_tree(tree_list, cursor * 2 + 1)

    return tree_node


def pre_order_tree(tree_node) -> list:
    """
    前序遍历二叉树。节点-左子树-右子树
    保留None
    :param tree_node:
    :return:
    """
    if not tree_node:
        return []

    result = []
    result.append(tree_node.val)
    result.extend(pre_order_tree(tree_node.left))
    result.extend(pre_order_tree(tree_node.right))

    return result


def in_order_tree(tree_node) -> list:
    """
    中序遍历二叉树。左子树-节点-右子树
    保留None
    :param tree_node:
    :return:
    """
    if not tree_node:
        return []

    result = []
    result.extend(in_order_tree(tree_node.left))
    result.append(tree_node.val)
    result.extend(in_order_tree(tree_node.right))

    return result


def post_order_tree(tree_node) -> list:
    """
    后续遍历二叉树。左子树-右子树-节点
    保留None
    :param tree_node:
    :return:
    """
    if not tree_node:
        return []

    result = []
    result.extend(post_order_tree(tree_node.left))
    result.extend(post_order_tree(tree_node.right))
    result.append(tree_node.val)

    return result


def level_order_tree(tree_node) -> list:
    """
    #102
    自顶向下按层遍历。1层-n层
    把每一层的节点放入队列中依次遍历，输出每一层的结果
    :param tree_node:
    :return:
    """
    if not tree_node:
        return []

    result = []

    queue = [[tree_node]]
    while queue:
        level = queue.pop(0)
        result.append([q.val for q in level])  # 当前这层的遍历结果

        next_level = []  # 获取下一层的需要遍历的节点
        for q in level:
            if q.left:
                next_level.append(q.left)
            if q.right:
                next_level.append(q.right)

        if next_level:
            queue.append(next_level)

    return result


a = load_list_to_binary_tree([1, 2, None, 4])
print(level_order_tree(a))
