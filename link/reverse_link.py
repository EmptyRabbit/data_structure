'''
链表反转
思路：原来指向后一个节点，现改为指向前一个节点，再变更头节点（原头节点指向尾节点后置null）
1、保存当前节点的next节点
2、当前next指向当前的前一个
3、变更当前节点为next
图解：https://blog.csdn.net/xyh269/article/details/70238501
'''
from single_link import SingleLinkList


class Node():
    '''链表节点'''

    def __init__(self, val, next_=None):
        self.val = val
        self.next_ = next_


class Solution:
    '''
        1->2->3->4
        4->3->2->1
    '''

    @staticmethod
    def reverseList(head: Node) -> Node:
        pre = None
        new_head = None

        while(head):
            next_ = head.next_
            head.next_ = pre
            new_head = head
            pre = head
            head = next_

        return new_head


if __name__ == '__main__':
    test = SingleLinkList()
    test.addAtHead(1)
    test.addAtIndex(1, 2)
    test.addAtIndex(2, 3)
    test.addAtIndex(3, 4)
    test.addAtIndex(4,5)
    print(test)

    test.head = Solution.reverseList(test.head)
    print(test)
