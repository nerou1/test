queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сводить детей в новый зоопарк',
    'пригласить мою жену на свидание',
    'где мне можно поспать',
    'заявление на'
]


def quantity_search(object: list) -> dict:
    '''Определяет колличество слов в запросе'''

    my_dict = {}
    one_percent = round(100 / len(object), 2)

    for element in object:
        count = len(element.split())
        string = f'из {count} слов'
        if string in my_dict:
            my_dict[string] += one_percent
        else:
            my_dict[string] = one_percent

    for key, value in my_dict.items():
        if int(value) - value == 0:
            my_dict[key] = int(value)
    return my_dict


if __name__ == '__main__':

    object = quantity_search(queries)

    for key, value in object.items():
        print(f'{key}: {value} %')

