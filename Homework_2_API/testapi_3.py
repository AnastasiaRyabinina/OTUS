# 3. Тестирование REST сервиса 3.
# Написать минимум 5 тестов для REST API сервиса: https://jsonplaceholder.typicode.com/.

import pytest
import requests
import cerberus


# Получение поста по id
def test_get_post_id(url, post_id):
    response = requests.get(url + "posts/" + str(post_id))
    schema = {
        'userId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'body': {'type': 'string'}
    }
    v = cerberus.Validator()
    # Проверяю схему и статус ответа
    assert v.validate(response.json(), schema)
    assert response.status_code == 200


# Получение постов заданного пользователя
@pytest.mark.parametrize('input_user, output_user',
                         [('5', 5), ('6', 6), ('10', 10)])
def test_get_post_id(url, input_user, output_user):
    response = requests.get(url + "posts?userId=" + str(input_user))
    res_json = response.json()
    assert response.status_code == 200
    for item in res_json:
        # Проверяю, что пользователь в ответе тот же, что подавался в параметрах
        assert item['userId'] == output_user


# Получение комментариев к заданному посту
@pytest.mark.parametrize('input_post, output_post',
                         [('2', 2), ('4', 4), ('90', 90)])
def test_get_post_comments(url, input_post, output_post):
    response = requests.get(f"{url}posts/{input_post}/comments")
    res_json = response.json()
    assert response.status_code == 200
    for item in res_json:
        # Проверяю, что номер поста в ответе тот же, что подавался в параметрах
        assert item['postId'] == output_post


# Создание нового поста
def test_post_post(data, headers):
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        headers=headers,
        json=data,
        verify=False
    )
    schema = {
        'userId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'body': {'type': 'string'}
    }
    v = cerberus.Validator()
    # Проверяю схему и статус ответа
    assert v.validate(response.json(), schema)
    assert response.status_code == 201


# Удаление поста
def test_delete_post(url, post_id):
    response = requests.delete(url + "posts/" + str(post_id))
    # Проверяю статус ответа и пустой json в ответе
    assert response.status_code == 200
    assert response.json() == {}
