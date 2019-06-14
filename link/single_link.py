
'''
单链表
'''


class Node():
    '''链表节点'''

    def __init__(self, val, next_=None):
        self.val = val
        self.next_ = next_


class SingleLinkList():
    '''
    单向链表数据结构
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
                result += f'{i}:{this.val}-'
                next_ = next_.next_

            return result
        return '空链表'

    def get(self, index: int) -> int:
        '''根据index查找下标为index的节点的值'''
        # index不在索引范围内返回-1
        if index <= -1 or index > self.length-1:
            return -1
        elif index == 0:
            return self.head.val
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
            self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.length <= 0:
            self.head = Node(val)
            self.length += 1
        else:
            next_ = self.head
            for _ in range(self.length):
                this = next_
                next_ = next_.next_

            this.next_ = Node(val)
            self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # index超出长度不添加
        if index > self.length:
            # print('index超出长度')
            return

        # index<=0添加为头节点
        if index <= 0:
            self.addAtHead(val)

        # index=长度，添加到末尾
        elif index == self.length:
            self.addAtTail(val)

        # 在index之前插入，this为index前一个节点
        elif index <= self.length-1:
            next_ = self.head
            for _ in range(index):
                this = next_
                next_ = next_.next_

            new_node = Node(val, this.next_)
            this.next_ = new_node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        '''
         根据index删除下标为index的节点的值，index超出索引不给删除
        '''
        if index >= self.length or index < 0:
            return

        # 若链表长度为空直接置空
        if self.length == 1:
            self.head = None
            self.length = 0
            return

        if index == 0:
            self.head = self.head.next_
            self.length -= 1
        elif index > -1 and index <= self.length-1:
            next_ = self.head
            for _ in range(index):
                this = next_
                next_ = next_.next_

            this.next_ = this.next_.next_
            self.length -= 1


if __name__ == '__main__':
    test = SingleLinkList()
    test.addAtHead(1)
    test.addAtIndex(0, 2)
    print(test)
