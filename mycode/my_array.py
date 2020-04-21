class Array(object):
    def __init__(self, size=32):
        self.size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return len(self._items)

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for _iter in self._items:
            yield _iter

    def __add__(self, value):
        self._items.append(value)

    def remove(self, value):
        self._items.remove(value)

    def pop(self):
        last_one = self._items.pop()
        return last_one


def test_array():
    size = 40
    a = Array(size)
    a[0] = 2
    a[1] = 3
    assert a[1] == 3
    assert a[2] is None
    assert len(a) == 40
    assert a.pop() is None
    assert len(a) == 39
    a.remove(2)
    assert len(a) == 38
