from src.parser import Parser
from src.utils import sort_by_date, final_sort
from config import Config


def main() -> str:
    """
    print the last 5 operations
    """
    manager = Parser()
    operations_list = sort_by_date(Config.FILE)
    operations_list_sorted = final_sort(operations_list)

    output = ''
    for operation in operations_list_sorted:
        operation['date'] = manager.convert_date(operation['date'])
        if 'from' in operation:
            operation['from'] = manager.convert_card_number(operation['from'], card_number=True)
        else:
            operation['from'] = ''
        operation['to'] = manager.convert_card_number(operation['to'], check=True)
        result = f"{operation['date']} {operation['description']}\n" \
                 f"{operation['from']} -> {operation['to']}\n" \
                 f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n\n"
        output += result
    return output


if __name__ == '__main__':
    print(main())
