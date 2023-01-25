class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.outer_cursor = 0  # первый элемент внешнего списка
        self.inner_cursor = 0  # первый элемент внутреннего списка
        self.outer_list_len = len(self.list_of_list)
        self.inner_list_len = len(self.list_of_list[self.outer_cursor])
        self.item = self.list_of_list.copy()
        self.counter = 0  # счетчик для проверки извлеченных элементов списков
        self.stop = False  # триггер для выброса исключения и завршения работы итератора
        self.count = -1  # счетчик для проверки можно ли возвращать значение итератором
        self.value = []  # список с финальными значениями элементов
        self.result = []  # список промежуточных значений элементов
        return self

    def __next__(self):
        while True:
            if self.stop:
                raise StopIteration
            self.counter = 0

            for i in self.item:
                if isinstance(i, list):
                    for j in i:
                        self.result.append(j)
                else:
                    self.result.append(i)
            self.item.pop(0)
            self.item = self.result

            for i in self.item:
                if not isinstance(i, list):
                    self.counter += 1

            if len(self.item) == self.counter:
                self.value = self.item.copy()
                self.count += 1
            self.result = []

            if self.count > -1:
                while self.count < len(self.item):
                    return self.value[self.count:self.count+1][0]
                else:
                    self.stop = True


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
