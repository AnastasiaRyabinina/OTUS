import pytest

# тестируемый метод string.count() возвращает количество вхождений
@pytest.mark.parametrize("test_input, item", [('no noyes yes', 'yes'), ('no nono', 'yes'), ('nonono no', 'no')])
def test_string_1(test_input, item):
    print('\nTEST 1. Проверяю, что количество вхождений больше либо равно 0.')
    assert test_input.count(item) >= 0


# тестируемый метод string.isalpha() определяет, состоит ли строка только из букв
@pytest.mark.parametrize("test_input", ['qwerty', 'Fgh78jFg!', '4096-a', 'HDDspeed_3'])
def test_string_2(test_input):
    print('\nTEST 2. Проверяю, что реультат работы метода string.isalpha() это True или False.')
    assert test_input.isalpha() == True or test_input.isalpha() == False


# тестируемый метод string.upper() преобразует все буквенные символы в заглавные
@pytest.mark.parametrize("test_input", ['qwerty', 'Fgh78jFg!', '4096-a', 'HDDspeed_3'])
def test_string_3(test_input):
    print('\nTEST 3. Проверяю, что буквенные символы строки стали заглавными.')
    result = test_input.upper()
    assert result.isupper() == True


# тестируемый метод string.join(<iterable>) объединяет список в строку
@pytest.mark.parametrize("test_input", [['fun', 'c', 'tion'], ['fix', 'ture', ' ', '№3']])
def test_string_4(test_input):
    print('\nTEST 4. Проверяю, что результат объеднения списка в строку существует.')
    assert ''.join(test_input) != None


# тестируемый метод string.zfill(<width>) дополняет строку нулями слева
@pytest.mark.parametrize("test_input", ['2', '1024', 'fix', 'Back to school!!'])
def test_string_54(test_input):
    print('\nTEST 5. Проверяю, что длина дополненной строки равна 16.')
    assert len(test_input.zfill(16)) == 16
