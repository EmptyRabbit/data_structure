class LinkNode():
    def __init__(self, val, _next):
        self.val = val
        self.next_node = _next

    def to_list(self):
        result = []
        _next_node = self
        while _next_node:
            result.append(self.val)
            _next_node = self.next_node
        return result


class SingleLink():
    """
    #707 设计链表的操作
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        获取链表index节点。index从0开始
        """
        if index < 0 or index > self.length - 1:
            return -1

        result = _next = self.head
        for _ in range(index + 1):
            result = _next
            _next = _next.next_node

        return result.val

    def add_head(self, val: int) -> None:
        """
        添加头节点
        """
        self.head = LinkNode(val, self.head)
        self.length += 1

    def add_tail(self, val: int) -> None:
        """
        添加尾节点，如果链表长度为0，添加头节点
        """
        if self.length <= 0:
            self.add_head(val)
            return

        result = _next = self.head
        for _ in range(self.length):
            result = _next
            _next = _next.next_node

        result.next_node = LinkNode(val, None)
        self.length += 1

    def add_at_index(self, index: int, val: int) -> None:
        """
        在index个节点前插入，index从0开始
        index等于链表长度时，插入为尾节点
        index等于链表长度，无任何操作
        index小于等于0，插入为头节点
        """
        if index > self.length:
            return

        if index <= 0:
            self.add_head(val)
            return

        result = _next = self.head
        for _ in range(index):
            result = _next
            _next = _next.next_node

        result.next_node = LinkNode(val, _next)
        self.length += 1

    def delete_index(self, index: int) -> None:
        """
        删除index节点，index从0开始
        """
        if index < 0 or index > self.length - 1:
            return

        if index == 0:
            self.head = self.head.next_node
            self.length -= 1
            return

        result = _next = self.head
        for _ in range(index):
            result = _next
            _next = _next.next_node

        result.next_node = _next.next_node
        self.length -= 1
