import json
import tempfile
from src.utils import *


def test_sort_by_date(operations):
    parser = Parser()
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as file:
        json.dump(operations, file)
    result = parser.read_file(operations)
    sort_list = sort_by_date(result)
    assert sort_list[0]['id'] == 1
    assert len(sort_list) == 3


def test_final_sort(operations):
    parser = Parser()
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as file:
        json.dump(operations, file)
    result = parser.read_file(operations)
    sorted_list = final_sort(result)
    assert len(sorted_list) == 2
    assert sorted_list[0]['state'] == 'EXECUTED'
