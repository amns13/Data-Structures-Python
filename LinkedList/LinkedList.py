class LinkedList:

    class _Node:
        __slots__ = '_data', '_next'

        def __init__(self, data=None, next=None):
            self._data = data
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0

    def value_at(self, k):
        if not 0 <= k < self._size:
            raise IndexError("Index out of bounds")

        cur = self._head
        for i in range(k):
            cur = cur._next

        return cur._data

    def push_front(self, val):
        new_node = self._Node(val, self._head)
        self._head = new_node
        self._size += 1

    def pop_front(self):
        if not self._head:
            raise IndexError("Empty Linked List")

        tmp = self._head
        self._head = self._head._next
        val = tmp._data
        tmp = None
        self._size -= 1
        return val

    def push_back(self, val):
        new_node = self._Node(val)
        if not self._head:
            self._head = new_node
            self._size += 1
            return

        cur = self._head
        while cur._next:
            cur = cur._next

        cur._next = new_node
        self._size += 1

    def pop_back(self):
        if not self._head:
            raise IndexError("Empty Linked List")

        cur = self._head
        prev = None

        while cur._next:
            prev = cur
            cur = cur._next

        res = cur._data
        if not prev:
            self._head = None
        else:
            prev._next = None
        cur = None
        self._size -= 1

        return res

    def insert(self, k, val):
        if not 0 <= k <= self._size:
            raise IndexError("Index out of bounds")

        if k == 0:
            self.push_front(val)
        elif k == self._size:
            self.push_back(val)
        else:
            cur = self._head
            for i in range(k-1):
                cur = cur._next
            new_node = self._Node(val, cur._next)
            cur._next = new_node
            self._size += 1

    def erase(self, k):
        if not 0 <= k < self._size:
            raise IndexError("Index out of bounds")

        if k == 0:
            self.pop_front()
        elif k == self._size - 1:
            self.pop_back()
        else:
            cur = self._head
            for i in range(k-1):
                cur = cur._next
            tmp = cur._next
            cur._next = tmp._next
            tmp = None
            self._size -= 1



    def __str__(self):
        lst = []
        cur = self._head

        while cur:
            lst.append(str(cur._data))
            cur = cur._next

        return ' -> '.join(lst)


def main():
    pass


if __name__ == '__main__':
    main()
