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
