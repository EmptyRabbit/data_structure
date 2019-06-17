'''
链表反转
'''
from single_link import SingleLinkList
import copy


class Node():
    '''链表节点'''

    def __init__(self, val, next_=None):
        self.val = val
        self.next_ = next_


class Solution:

    @staticmethod
    def reverseList(head: Node) -> Node:
        this = head
        pre = None
        while this.next_:
            guard = Node(this.next_.val, this.next_.next_)
            if pre:
                pre.next_ = guard

            this.next_ = guard.next_
            guard.next_ = this

            if not pre:
                head = guard
                pre = head

        return head


if __name__ == '__main__':
    test = SingleLinkList()
    test.addAtHead(1)
    test.addAtIndex(1, 2)
    test.addAtIndex(2, 3)
    print(test)

    test.head = Solution.reverseList(test.head)
    print(test)
