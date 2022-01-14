
import config
import requests
import unidecode
from typing import TypeVar, List

T = TypeVar('T')


def get_page(uri: str, *args, **kwargs):
    headers = {
        'User-Agent': config.USER_AGENT
    }
    custom_headers = kwargs.get('headers')
    if custom_headers is not None:
        headers = {**headers, **custom_headers}
        del kwargs['headers']
    return requests.get(uri, *args, headers=headers, **kwargs)


def parse_search_query(name: str, separator='-'):
    normalized = unidecode.unidecode(name).lower()
    result = separator.join(normalized.split())
    return result


def prompt_options(
        title: str, prompt_text: str,
        item_list: List[T],
        not_exists_message: str = "Nada foi encontrado.") -> T:
    item_quantity = len(item_list)
    if(item_quantity == 0):
        print(not_exists_message)
        return None
    print(title.format(length=item_quantity), *
          map(lambda item: f"[{item[0] + 1}]: {item[1].title}", enumerate(item_list)), sep="\n  ")
    print()
    selected_item_index = None
    while selected_item_index is None or selected_item_index > item_quantity - 1 or selected_item_index < 0:
        item_index = input(prompt_text.format(length=item_quantity))
        if item_index.isdigit():
            selected_item_index = int(item_index) - 1
        elif item_index.strip() == '':
            selected_item_index = 0
    selected_item = item_list[selected_item_index]
    return selected_item