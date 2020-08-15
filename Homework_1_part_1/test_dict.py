import pytest

# тестируемый метод dict.get() - получение значения по указанному ключу
def test_dict_1(fixture_return_dict):
    print('\nTEST 1. Проверяю, что значение, полученное по ключу, является целым числом.')
    result = fixture_return_dict.get('black')
    assert result % 1 == 0


# тестируемый метод dict.update() - обновление словаря
def test_dict_2(fixture_return_dict):
    print('\nTEST 2. Проверяю, что после обновления словарь увелилчился на длину второго словаря.')
    l = len(fixture_return_dict)
    fixture_return_dict.update({'purple' : 23, 'grey':48})
    assert len(fixture_return_dict) == l + 2


# тестируемый метод dict.get() - возвращает значение по указанному ключу
def test_dict_3(fixture_return_dict):
    print('\nTEST 3. Проверяю, что метод возвращает то же значние, что и непосредственное обращение к словарю с ключом.')
    my_value = fixture_return_dict.get('red')
    assert my_value == fixture_return_dict['red']


# тестируемый метод dict.pop() - удаляет ключ и возвращает значение.
def test_dict_4(fixture_return_dict, fixture_return_color):
    print('\nTEST 4. Проверяю, что длина словаря уменьшилась на единицу, либо ключ не был найден.')
    l = len(fixture_return_dict)
    result = fixture_return_dict.pop(fixture_return_color, 'no_key')
    assert len(fixture_return_dict) == l - 1 or result == 'no_key'


# тестируемый метод dict.clear() - очищает словарь.
def test_dict_5(fixture_return_dict):
    print('\nTEST 5. Проверяю, что после очищения словаря его длина равно 0.')
    fixture_return_dict.clear()
    assert len(fixture_return_dict) == 0