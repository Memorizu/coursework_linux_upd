from src.parser import Parser


def sort_by_date(data) -> list:
    """
    :return:  sorted list by date
    """
    parser = Parser()
    operations = parser.read_file(data)

    sorted_list = sorted(operations, key=lambda x: x.get('date', ''), reverse=True)
    return sorted_list


def final_sort(sorted_list) -> list:
    """
    :return: last 5 EXECUTED operations
    """
    for operation in sorted_list:
        if operation and operation['state'] != 'EXECUTED':
            sorted_list.remove(operation)
    return sorted_list[:5]
