import types


def flat_generator(list_of_lists):
    outer_cursor = 0
    inner_cursor = 0
    while outer_cursor < len(list_of_lists):
        inner_list_len = len(list_of_lists[outer_cursor])
        if inner_list_len > inner_cursor:
            yield list_of_lists[outer_cursor][inner_cursor]
            inner_cursor += 1
        else:
            outer_cursor += 1
            inner_cursor = 0


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
