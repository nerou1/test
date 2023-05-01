import pytest
from task_1 import filter_the_list

my_list = [[
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']}
],
    [
        {'visit1': ['Питер', 'Малибу']},
        {'visit3': ['Владимир', 'Курс']}
    ],
    [
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
    ]]


@pytest.mark.parametrize('my_list', my_list)
def test_len(my_list):
    result = filter_the_list(my_list)
    assert len(result) in (0, 2, 6), f'Длина {len(result)} не верна'


@pytest.mark.parametrize('my_list', my_list)
def test_on_list(my_list):
    result = filter_the_list(my_list)
    assert type(result) == list, 'Результат не является списком'
    assert type(result) not in (int, float, tuple, dict, set, str, bool)


@pytest.mark.parametrize('my_list', my_list)
def test_find_Russia(my_list):
    result = filter_the_list(my_list)
    for element in result:
        for values in element.values():
            assert 'Россия' in values, 'Не найдено слово Россия'


if __name__ == '__main__':
    pytest.main()



