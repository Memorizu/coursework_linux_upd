from config import Config
from src.utils import *


def test_sort_by_date():
    parser = Parser()
    data = parser.read_file(Config.TEST_FILE)
    sort_list = sort_by_date(data)
    assert sort_list[0]['id'] == 1
    assert len(sort_list) == 4


def test_final_sort():
    parser = Parser()
    data = parser.read_file(Config.TEST_FILE)
    sorted_list = final_sort(data)
    assert len(sorted_list) == 3
    assert sorted_list[0]['state'] == 'EXECUTED'
