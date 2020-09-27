# 4. Реализуйте в отдельном модуле (файле) тестовую функцию которая будет принимать 2 параметра:
# url - должно быть значение по умолчанию https://ya.ru
# status_code - значение по умолчанию 200
# пример запуска pytest test_module.py --url=https://mail.ru --status_code=200

import pytest
import requests


def test_status_code(url, status_code):
    response = requests.get(url)
    assert response.status_code == int(status_code)
