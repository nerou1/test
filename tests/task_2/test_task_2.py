import pytest
from task_2 import dictionary_filter

ids = [
    {'user1': [213, 213, 213, 15, 213],
     'user2': [54, 54, 119, 119, 119],
     'user3': [213, 98, 98, 35]
     },
    {'user1': [213, 213, 213, 15, 213],
     'user2': [54, 54, 119, 119, 119],
     'user3': [213, 98, 98, 35],
     'user4': [],
     'user5': [12, 12, 12, 12],
     'user6': ['yes', 'no', '', False]
     }
]


@pytest.mark.parametrize('ids', ids)
def test_len(ids):
    result = dictionary_filter(ids)
    assert len(result) > 0, f'Длина {len(result)} не верна'


@pytest.mark.parametrize('ids', ids)
def test_on_list(ids):
    result = dictionary_filter(ids)
    assert type(result) == list, 'Результат не является списком'
    assert type(result) not in (int, float, tuple, dict, set, str, bool)


@pytest.mark.parametrize('ids', ids)
def test_is_instance(ids):
    result = dictionary_filter(ids)
    assert (213 in result) or (False in result), 'Не найдено слово False или число 213'


if __name__ == '__main__':
    pytest.main()



