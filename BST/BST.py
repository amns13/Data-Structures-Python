from collections import deque


class BST:

    class _Node:
        __slots__ = '_data', '_lc', '_rc'
        
        def __init__(self, data, lc=None, rc=None):
            self._data = data
            self._lc = None
            self._rc = None

    def __init__(self):
        self._root = None

    def insert(self, val):
        self._root = self._insert(self._root, val)

    def search(self, key):
        return self._search(self._root, key)

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def inorder(self):
        self._inorder(self._root)
        print()

    def levelorder(self):
        node = self._root
        q = deque()
        q.append(node)

        while len(q) > 0:
            cur = q.popleft()
            print(cur._data, end=' ')
            if cur._lc:
                q.append(cur._lc)
            if cur._rc:
                q.append(cur._rc)

        print()


    def _min(self, node):
        if node is None:
            raise ValueError("Root node is None")

        while node._lc:
            node = node._lc
        return node._data

    def _max(self, node):
        if node is None:
            raise ValueError("Root node is None")

        while node._rc:
            node = node._rc
        return node._data

    def _insert(self, node, val):
        if node is None:
            return self._Node(val)

        if val == node._data:
            raise ValueError(f"Node with value {val} exists already")
        elif val < node._data:
            node._lc = self._insert(node._lc, val)
        else:
            node._rc = self._insert(node._rc, val)

        return node

    def _inorder(self, node):
        if node is not None:
            self._inorder(node._lc)
            print(node._data, end=' ')
            self._inorder(node._rc)


    def _search(self, node, key):
        if node is None:
            return False

        if key < node._data:
            return self._search(node._lc, key)
        elif key > node._data:
            return self._search(node._rc, key)
        else:
            return True

    def _remove(self, node, key):
        if node is None:
            raise ValueError(f"No node with value {key}")

        if key < node._data:
            node._lc = self._remove(node._lc, key)
        elif key > node._data:
            node._rc = self._remove(node._rc, key)
        else:
            if not (node._lc or node._rc):
                node = None
            elif not node._lc:
                tmp = node._rc
                node._rc = None
                node = tmp
            elif not node._rc:
                tmp = node._lc
                node._lc = None
                node = tmp
            else:
                min_in_right = self._min(node._rc)
                node._data = min_in_right
                node._rc = self._remove(node._rc, min_in_right)

        return node




