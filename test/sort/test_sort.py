import json

from sort.selection_sort import selection_sort
from sort.insertion_sort import insertion_sort


def test_selection_sort():
    with open('/Users/zhouxin.qiu/Documents/mygit/data_structure/test/data/sort/case.json') as f:
        case = json.load(f)
    assert selection_sort(case) == sorted(case)


def test_insertion_sort():
    with open('/Users/zhouxin.qiu/Documents/mygit/data_structure/test/data/sort/case.json') as f:
        case = json.load(f)
    assert insertion_sort(case) == sorted(case)
