import pytest

# тестируемый метод set.add()
def test_set_1(fixture_return_set_and_len, fixture_return_element_with_params):
    print('\nTEST 1. Проверяю, что при добавлении элемента в множество увеличивается длина множества.')
    if fixture_return_element_with_params not in fixture_return_set_and_len[0]:
        fixture_return_set_and_len[0].add(fixture_return_element_with_params)
        assert len(fixture_return_set_and_len[0]) == fixture_return_set_and_len[1] + 1


# тестируемый метод set.discard()
def test_set_2(fixture_return_set_and_len, fixture_return_element_with_params):
    print('\nTEST 2. Проверяю, что при удалении элемента из множества длина множества уменьшается.')
    if fixture_return_element_with_params in fixture_return_set_and_len[0]:
        fixture_return_set_and_len[0].discard(fixture_return_element_with_params)
        assert len(fixture_return_set_and_len[0]) == fixture_return_set_and_len[1] - 1


# тестируемый метод set.copy()
def test_set_3(fixture_return_set_and_len):
    print('\nTEST 3. Проверяю, что копия множества равна исходному множеству.')
    my_set = fixture_return_set_and_len[0].copy()
    assert my_set == fixture_return_set_and_len[0]


# тестируемый метод set.union()
def test_set_4(fixture_return_set_and_len, fixture_return_list_with_params):
    print('\nTEST 4. Проверяю, что длина объединенного множества не больше суммы длин подмножеств.')
    second_set = set(fixture_return_list_with_params)
    union_result = fixture_return_set_and_len[0].union(second_set)
    assert len(union_result) <= len(second_set) + len(fixture_return_set_and_len[0])


# тестируемый метод set.issuperset()
def test_set_5(fixture_return_set_and_len, fixture_return_list_with_params):
    print('\nTEST 5. Проверяю, что результатом проверки на подмножество является True или False.')
    second_set = set(fixture_return_list_with_params)
    result = fixture_return_set_and_len[0].issuperset(second_set)
    assert result == True or result == False
