
'''
双向链表
'''


class Node():
    '''链表节点'''

    def __init__(self, val, next_=None, pre=None):
        self.val = val
        self.pre = pre
        self.next_ = next_


class SingleLinkList():
    '''
    双向链表数据结构
    index均从0开始，第index个代表下标为index的那个节点
    '''

    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        '''输出链表 序号:值'''
        result = ''
        if self.length:
            next_ = self.head
            for i in range(self.length):
                this = next_
                result += f'{i}:{this.val},{this.pre.val if this.pre else "none"}-'
                next_ = next_.next_

            return result
        return '空链表'

    def get(self, index: int) -> int:
        '''根据index查找下标为index的节点的值'''
        # index不在索引范围内返回-1
        if index <= -1 or index > self.length-1:
            return -1
        else:
            next_ = self.head
            for _ in range(index+1):
                this = next_
                next_ = next_.next_

            return this.val

    def addAtHead(self, val: int) -> None:
        if self.length <= 0:
            self.head = Node(val)
        else:
            new_node = Node(val, self.head)
            self.head.pre = new_node
            self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.length <= 0:
            self.addAtHead(val)
        else:
            next_ = self.head
            for _ in range(self.length):
                this = next_
                next_ = next_.next_

            this.next_ = Node(val, None, this)
            self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # index超出长度不添加
        if index > self.length:
            # print('index超出长度')
            return

        # index<=0添加为头节点
        if index <= 0:
            self.addAtHead(val)
        else:
            # index=长度，添加到末尾
            if index == self.length:
                self.addAtTail(val)
            # 在index之前插入
            elif index <= self.length-1:
                next_ = self.head
                for _ in range(index+1):
                    this = next_
                    next_ = next_.next_

                new_node = Node(val, this, this.pre)
                this.pre.next_ = new_node
                this.pre = new_node

                self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        '''
         根据index删除下标为index的节点的值，index超出索引不给删除
        '''
        if index >= self.length or index < 0:
            return

        # 若链表长度为空直接置空
        if self.length == 1 or index == 0:
            self.head = self.head.next_
        elif index > -1 and index <= self.length-1:
            next_ = self.head
            for _ in range(index+1):
                this = next_
                next_ = next_.next_

            this.pre.next_ = this.next_
            if this.next_:
                this.next_.pre = this.pre

        self.length -= 1


if __name__ == '__main__':
    test = SingleLinkList()
    test.addAtHead(1)
    test.addAtIndex(0, 2)
    test.addAtHead(3)
    print(test)
