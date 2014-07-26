
from copy import deepcopy


class DataFactory(object):
    """Simple class that returns a deepcopy from `data` dict. This is needed to
    prevent data consumers from mistakenly modifying global data.
    """
    def __init__(self, data):
        self.data = data

    def __getitem__(self, item):
        """Return deepcopy of data item."""
        return deepcopy(self.data[item])

    def __getattr__(self, item):
        """Return deepcopy of data item."""
        return self.__getitem__(item)


_data = {
    'find': [
        {'name': 'barney',  'age': 36, 'blocked': False},
        {'name': 'fred',    'age': 40, 'blocked': True},
        {'name': 'pebbles', 'age': 1,  'blocked': False}
    ],
    'filter_': [
        {'name': 'barney', 'age': 36, 'blocked': False},
        {'name': 'fred',   'age': 40, 'blocked': True}
    ],
    'sample': [1, 2, 3, 4, 5, 6],
}


data = DataFactory(_data)


def reduce_callback0(total, num, *args):
    return total + num


def reduce_callback1(result, num, key):
    result[key] = num * 3
    return result


def reduce_right_callback0(a, b, *args):
    return a + b