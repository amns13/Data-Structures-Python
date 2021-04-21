import ctypes


MIN_CAPACITY = 16   # Minimum Capacity
GROWTH_FACTOR = 2
SHRINK_FACTOR = 4


class DynamicArray:
    '''
    Implementation of a Dynamic Array.
    List.
    '''
    
    def __init__(self):
        self._n = 0
        self._capacity = MIN_CAPACITY
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("Index out of bounds")
        return self._A[k]

    def __str__(self):
        lst = []
        for i in range(self._n):
            lst.append(str(self._A[i]))

        return ', '.join(lst)

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def _resize(self, c):
        B = self._make_array(c)
        
        for i in range(self._n):
            B[i] = self._A[i]

        self._A = B
        self._capacity = c

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(GROWTH_FACTOR * self._capacity)

        self._A[self._n] = obj
        self._n += 1

    def pop(self):
        if self._n == 0:
            raise IndexError("Empty list")

        if self._capacity > MIN_CAPACITY \
                and SHRINK_FACTOR * self._n == self._capacity:
            self._resize(self._capacity // GROWTH_FACTOR)

        obj = self._A[self._n - 1]
        self._A[self._n - 1] = None
        self._n -= 1

        return obj

    def insert(self, k, value):
        if not 0 <= k <= self._n:
            raise IndexError("Index out of bounds.")

        if self._n == self._capacity:
            self._resize(GROWTH_FACTOR * self._capacity)

        for i in range(self._n, k, -1):
            self._A[i] = self._A[i-1]

        self._A[k] = value
        self._n += 1

    def remove(self, val):
        for i in range(self._n):
            if self._A[i] == val:
                if self._capacity > MIN_CAPACITY \
                        and SHRINK_FACTOR * self._n == self._capacity:
                    self._resize(self._capacity // GROWTH_FACTOR)

                for j in range(i, self._n-1):
                    self._A[i] = self._A[i+1]

                self._A[self._n-1] = None
                self._n -= 1
                return

        raise ValueError("Value not found")


def main():
    a = DynamicArray()

    for i in range(10):
        a.append(i)

    print('Length: ', len(a))
    print(a)
    print('Capacity: ', a._capacity)

    print('popped: ', a.pop())
    print('popped: ', a.pop())
    print('popped: ', a.pop())

    print('Length: ', len(a))
    print(a)
    print('Capacity: ', a._capacity)

    for i in range(20, 30):
        a.append(i)

    print('Length: ', len(a))
    print(a)
    print('Capacity: ', a._capacity)

    a.insert(3, 300)
    a.insert(5, 500)

    print(a)

    a.remove(23)
    print(a)

    for i in range(10):
        a.pop()

    print('Length: ', len(a))
    print(a)
    print('Capacity: ', a._capacity)

    a.pop()

    print('Length: ', len(a))
    print(a)
    print('Capacity: ', a._capacity)

    for i in range(len(a)):
        print(a[i], end=' -> ')
    print()


if __name__ == '__main__':
    main()




