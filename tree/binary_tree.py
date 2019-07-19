

# 二叉树数据结构
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 通过列表构建二叉树（前序遍历列表）
def build_tree(self, tree, data, i):
    while i <= len(data):
        if data[i] == None:
            return

        else:
            tree = TreeNode(data[i])
            tree.left = build_tree(tree, data, 2 * i + 1)
            tree.right = build_tree(tree, data, 2 * i + 2)

        return tree


# 二叉树前序遍历
result = []


def preorderTraversal(self, root):
    if root:
        self.result.append(root.val)
    if root.left:
        self.preorderTraversal(root.left)
    if root.right:
        self.preorderTraversal(root.right)

    return self.result


# 二叉树中序遍历
result = []


def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root.left:
        self.inorderTraversal(root.left)

    if root:
        self.result.append(root.val)

    if root.right:
        self.inorderTraversal(root.right)

    return self.result


# 二叉树中序遍历
result = []


def postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root.left:
        self.postorderTraversal(root.left)

    if root.right:
        self.postorderTraversal(root.right)

    if root:
        self.result.append(root.val)

    return self.result


# 二叉树层序遍历
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = [root]
        result = []
        next = q[:]
        while next:
            q = next[:]
            next = []
            each = []
            for i in q:
                each.append(i.val)
                if i.left:
                    next.append(i.left)
                if i.right:
                    next.append(i.right)

            result.append(each)

        return result


# 自顶向下最大深度（类似前序遍历）
result = 0


def get_max_length(root, depth):
    if not root:
        return

    if not root.left and not root.right:
        result = max(depth, result)

    get_max_length(root.left, depth + 1)
    get_max_length(root.right, depth + 1)


# 自底向上最大深度（类似后序遍历）
def get_max_lenght_from_leaf(root):
    if not root:
        return 0

    left = get_max_lenght_from_leaf(root.left)
    right = get_max_lenght_from_leaf(root.right)

    return max(left, right) + 1


# 判断是否是对称二叉树（使用层序遍历）
def isSymmetric(root):
    """
           :type root: TreeNode
           :rtype: bool
           """

    result = []

    q = [root]
    next = q[:]

    symm = True

    while next:

        each = []
        q = next[:]
        next = []
        for i in q:
            if i:
                each.append(i.val)
            else:
                each.append(i)

            if i:
                next.append(i.left)
                next.append(i.right)

        each_len = len(each)
        for i in range(int(each_len)):
            if each[i] != each[-(i + 1)]:
                symm = False
                break

        result.append(each)

    return symm


# 判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和
class Solution:
    def __init__(self):
        self.rsum = 0
        self.result = False

    def hasPathSum(self, root, sum, rsum=0):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return self.result

        self.rsum += root.val
        print(root.val)

        if not root.left and not root.right:
            if self.rsum == sum:
                self.result = True
                return self.result

        self.hasPathSum(root.left, sum, rsum)
        self.hasPathSum(root.right, sum, rsum)
        self.rsum = self.rsum - root.val

        return self.result
