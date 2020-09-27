# 1. Тестирование REST сервиса 1
# Написать минимум 5 тестов для REST API сервиса: https://dog.ceo/dog-api/.
import pytest
import requests
import cerberus


def test_random_image():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    schema = {
        "message": {"type": "string"},
        "status": {"type": "string"}
    }
    v = cerberus.Validator()
    # Проверяю схему и статус ответа
    assert v.validate(response.json(), schema)
    assert response.json()['status'] == 'success'


def test_random_image_3():
    response = requests.get("https://dog.ceo/api/breeds/image/random/3")
    schema = {
        "message": {"type": "list"},
        "status": {"type": "string"}
    }
    v = cerberus.Validator()
    trio = response.json()['message']
    # Проверяю количество элементов в списке, схему и статус ответа
    assert len(trio) == 3
    assert v.validate(response.json(), schema)
    assert response.json()['status'] == 'success'


def test_by_breed():
    response = requests.get("https://dog.ceo/api/breed/terrier/images/random")
    schema = {
        "message": {"type": "string"},
        "status": {"type": "string"}
    }
    v = cerberus.Validator()
    mes = response.json()['message']
    # Проверяю наличие названия породы в сообщении, схему и статус ответа
    assert mes.find('terrier') > 0
    assert v.validate(response.json(), schema)
    assert response.json()['status'] == 'success'


@pytest.mark.parametrize("breed", ['mastiff', 'boxer', 'husky'])
def test_real_breeds(breed):
    response = requests.get("https://dog.ceo/api/breed/" + breed + "/images/random")
    # Проверяю статус ответа для существующих пород
    assert response.json()['status'] == 'success'


@pytest.mark.parametrize("breed", ['cat', 'mouse', 'horse'])
def test_unreal_breeds(breed):
    response = requests.get("https://dog.ceo/api/breed/" + breed + "/images/random")
    # Проверяю статус ответа для несуществующих пород
    assert response.json()['status'] == 'error'
