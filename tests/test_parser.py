import json
import tempfile
import pytest
import os
from src.parser import Parser


class TestParser:

    dates = [
        ('2022-05-02T10:25:30.000Z', '02.05.2022'),
        ('2019-08-26T10:50:58.294041', '26.08.2019'),
        ('2019-04-04T23:20:05.206878', '04.04.2019')
    ]

    card_num = [
        ("Счет 75106830613657916952", "Счет 7510 68** **** 6952"),
        ("Счет 44812258784861134719", "Счет 4481 22** **** 4719")
    ]

    check_num = [
        ("Счет 75651667383060284188", "Счет **4188"),
        ("Счет 74489636417521191160", "Счет **1160")
    ]

    @pytest.mark.parametrize("date, correct_date", dates)
    def test_convert_date(self, date, correct_date):
        parser = Parser()
        assert parser.convert_date(date) == correct_date

    def test_convert_date_error(self):
        parser = Parser()
        with pytest.raises(TypeError):
            parser.convert_date(12345)

    def test_read_file(self, operations):
        parser = Parser()
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as data_file:
            json.dump(operations, data_file)
        result = parser.read_file(data_file.name)
        assert result == operations
        os.unlink(data_file.name)

    @pytest.mark.parametrize("card_number, correct_card_number", card_num)
    def test_convert_card_number(self, card_number, correct_card_number):
        parser = Parser()
        assert parser.convert_card_number(card_number, card_number=True) == correct_card_number

    @pytest.mark.parametrize("check_number, correct_check_number", check_num)
    def test_convert_check_number(self, check_number, correct_check_number):
        parser = Parser()
        assert parser.convert_card_number(check_number, check=True) == correct_check_number
