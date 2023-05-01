geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def filter_the_list(object: list) -> list:
    '''Функция отфильтровывает словарь в котором встречается слово Россия'''

    filtr = []
    for element in object:
        for country in element.values():
            if 'Россия' in country:
                filtr.append(element)
    return filtr


if __name__ == '__main__':

    for element in filter_the_list(geo_logs):
        print(element)
