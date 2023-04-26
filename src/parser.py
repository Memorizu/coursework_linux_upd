import json
from typing import Union


class Parser:

    def read_file(self, data) -> Union[list, dict]:
        """
        read data from json file
        :return: list of operations
        """
        if isinstance(data, str):
            with open(data) as file:
                return json.load(file)
        elif isinstance(data, list):
            return data
        else:
            raise TypeError('Unsupported data type')

    @staticmethod
    def convert_date(date: str) -> str:
        """
        converts the data to the desired format
        :return: formatted date
        """
        return f'{date[8:10]}.{date[5:7]}.{date[:4]}'

    def convert_card_number(self, number: str, check=False, card_number=False) -> str:
        """
        converted number of check or card number to the desired format
        :param number: string with name of check and number
        :param check: number of check
        :param card_number: number of card
        :return: formatted number depending on the passed argument
        """
        num_list = number.split()
        for i in num_list:
            if i.isdigit():
                num_list.remove(i)
                if card_number:
                    converted_number = self.__convert_card_digits(i)
                    num_list.append(converted_number)
                if check:
                    converted_number = self.__convert_check_digits(i)
                    num_list.append(converted_number)
        return ' '.join(num_list)

    def __convert_check_digits(self, number: str) -> str:
        return f'**{number[-4:len(number)]}'

    def __convert_card_digits(self, number: str) -> str:
        return f'{number[:4]} {number[4:6]}** **** {number[-4:len(number)]}'
