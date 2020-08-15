import pytest

# ----- fixtures for lists -----
@pytest.fixture
def fixture_return_list_and_len():
    my_list = ['apple','banana','coconut','grape','orange','apple']
    return my_list, len(my_list)

new_lists = (['one', 'two', 'three', 'four', 'five'], ['tomato','grape','potato'], ['apple'])

@pytest.fixture(params=new_lists)
def fixture_return_list_with_params(request):
    return request.param

new_elements = ('grape', 'banana', 'fig', 'pear')

@pytest.fixture(params=new_elements)
def fixture_return_element_with_params(request):
    return request.param


# ----- fixtures for sets -----
@pytest.fixture
def fixture_return_set_and_len(fixture_return_list_and_len):
    my_set = set(fixture_return_list_and_len[0])
    return my_set, len(my_set)


# ----- fixtures for dicts -----
@pytest.fixture
def fixture_return_dict():
    my_dict = {'red': 1, 'orange': 2, 'yellow': 3, 'green': 4, 'black': 99}
    return my_dict

colors = ('red', 'orange', 'blue', 'purple', 'metallic')

@pytest.fixture(params=colors)
def fixture_return_color(request):
    return request.param
