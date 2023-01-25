class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.outer_cursor = 0  # первый элемент внешнего списка
        self.inner_cursor = 0  # первый элемент внутреннего списка
        self.item = []
        return self

    def __next__(self):
        while self.outer_cursor < len(self.list_of_list):
            self.inner_list_len = len(self.list_of_list[self.outer_cursor])
            if self.inner_list_len <= self.inner_cursor:
                self.inner_cursor = 0
                self.outer_cursor += 1
            else:
                self.item = self.list_of_list[self.outer_cursor][self.inner_cursor]
                self.inner_cursor += 1
                return self.item
        else:
            raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
