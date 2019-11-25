class LinkNode():
    def __init__(self, val, _next):
        self.val = val
        self.next_node = _next


class SingleLink():
    """
    #707设计链表的操作
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        index start with 0
        """
        if index < 0 or index > self.length:
            return -1

        result = _next = self.head
        for _ in range(index):
            result = _next
            _next = _next.next_node

        return result.val

    def add_head(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        self.head = LinkNode(val, self.head)
        self.length += 1

    def add_tail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        result = _next = self.head
        for _ in range(self.length):
            result = _next
            _next = _next.next_node

        result.next_node = LinkNode(val, None)

    def add_at_index(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
