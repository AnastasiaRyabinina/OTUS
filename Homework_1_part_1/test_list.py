import pytest

# тестируемый метод list.append()
def test_list_1(fixture_return_list_and_len):
    superlist = fixture_return_list_and_len[0]
    lenght_before = fixture_return_list_and_len[1]
    superlist.append('new_list_element')
    print('\nTEST 1. Проверяю, что длина списка увеличилась на 1, и последний элемент списка имеет нужное значение.')
    assert len(superlist) == lenght_before + 1 and superlist[lenght_before] == 'new_list_element'


# тестируемый метод list.pop()
def test_list_2(fixture_return_list_and_len):
    superlist = fixture_return_list_and_len[0]
    lenght_before = fixture_return_list_and_len[1]
    superlist.pop()
    print('\nTEST 2. Проверяю, что длина списка уменьшилась на 1.')
    assert len(superlist) == lenght_before - 1


# тестируемый метод list.clear()
def test_list_3(fixture_return_list_and_len):
    superlist = fixture_return_list_and_len[0]
    superlist.clear()
    print('\nTEST 3. Проверяю, что список пустой.')
    assert len(superlist) == 0


# тестируемый метод list.index(), параметризация через фикстуру
def test_list_4(fixture_return_list_and_len, fixture_return_element_with_params):
    superlist = fixture_return_list_and_len[0]
    print('\nTEST 4. Проверяю, что возвращается позиция элемента внутри списка.')
    if superlist.count(fixture_return_element_with_params) == 0:
        pass
    else:
        assert superlist.index(fixture_return_element_with_params) < len(superlist)


# тестируемый метод list.extend(), параметризация через фикстуру
def test_list_5(fixture_return_list_and_len, fixture_return_list_with_params):
    superlist = fixture_return_list_and_len[0]
    lenght_before = fixture_return_list_and_len[1]
    superlist.extend(fixture_return_list_with_params)
    print('\nTEST 5. Проверяю, что список увеличился на длину нового списка')
    assert len(superlist) == lenght_before + len(fixture_return_list_with_params)
