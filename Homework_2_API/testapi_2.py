# 2. Тестирование REST сервиса 2
# Написать минимум 5 тестов для REST API сервиса: https://www.openbrewerydb.org/
import pytest
import requests
import cerberus


# Получение пивоварни по заданному id
def test_get_by_id(url, brewery_id):
    response = requests.get(url + "breweries/" + str(brewery_id))
    schema = {
        'id': {'type': 'number'},
        'name': {'type': 'string'},
        'brewery_type': {'type': 'string', 'allowed': ["micro",
                                                       "regional",
                                                       "large",
                                                       "planning",
                                                       "brewpub",
                                                       "bar",
                                                       "contract",
                                                       "proprietor"]},
        'street': {'type': 'string'},
        'city': {'type': 'string'},
        'state': {'type': 'string'},
        'postal_code': {'type': 'string'},
        'country': {'type': 'string'},
        'longitude': {'type': 'string', 'nullable': True},
        'latitude': {'type': 'string', 'nullable': True},
        'phone': {'type': 'string'},
        'website_url': {'type': 'string'},
        'updated_at': {'type': 'string'}
    }
    v = cerberus.Validator()
    # print(response.json())
    # Проверяю схему и статус ответа
    assert v.validate(response.json(), schema)
    assert response.status_code == 200


# Получение списка пивоварен, расположенных в заданном городе
@pytest.mark.parametrize('input_city, output_city',
                         [('Florence', 'Florence'),
                          ('Birmingham', 'Birmingham'),
                          ('Carlsbad', 'Carlsbad')])
def test_list_by_city(url, input_city, output_city):
    response = requests.get(url + 'breweries?by_city=' + input_city)
    res_json = response.json()
    for item in res_json:
        # Проверяю, что город из входящих параметров и город в ответе одинаковые
        assert item['city'] == output_city


# Получение списка пивоварен, расположенных в заданном штате
@pytest.mark.parametrize('input_state, output_state',
                         [('California', 'California'),
                          ('Alabama', 'Alabama'),
                          ('Washington', 'Washington')])
def test_list_by_state(url, input_state, output_state):
    response = requests.get(url + 'breweries?by_state=' + input_state)
    res_json = response.json()
    for item in res_json:
        # Проверяю, что штат из входящих параметров и штат в ответе одинаковые
        assert item['state'] == output_state


# Постаничный вывод списка пивоварен
def test_per_page(url, per_page):
    response = requests.get(url + 'breweries?per_page=' + str(per_page))
    # Проверяю, что длина ответа равна заданному во входящих параметрах числу объектов на страницу
    assert len(response.json()) == int(per_page)


# Поиск пивоварен
def test_search_by_query(url, query="bear"):
    response = requests.get(url + 'breweries/search?query=' + query)
    result = response.text
    # Проверяю, что ответ содержит хотя бы одно совпадение с запросом, либо текст ответа пустой
    assert result.count(query) > 0 or result == '[]'
