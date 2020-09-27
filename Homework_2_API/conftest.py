import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        # URL для второго задания
        default="https://api.openbrewerydb.org/",
        # URL для третьего задания
        # default="https://jsonplaceholder.typicode.com/",
        # URL для четвертого задания
        # default="https://ya.ru/",
        help="This is request url"
    )

    parser.addoption(
        "--id",
        default=1,
        help="This is id of brewery"
    )

    parser.addoption(
        "--page",
        default=5,
        choices=["5", "15", "25", "50"],
        help="This is count of items on page"
    )

    parser.addoption(
        "--post",
        default=1,
        help="This is id of post"
    )

    parser.addoption(
        "--status_code",
        default=200,
        help="This is status code"
    )

@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def brewery_id(request):
    return request.config.getoption("--id")

@pytest.fixture
def per_page(request):
    return request.config.getoption("--page")

@pytest.fixture
def post_id(request):
    return request.config.getoption("--post")

@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")


@pytest.fixture
def data():
    return {
        "title": "Machine learning",
        "body": "Machine learning is closely related to computational statistics, which focuses on making predictions using computers.",
        "userId": 121
    }

@pytest.fixture
def headers():
    return {
        "Content-type": "application/json; charset=UTF-8"
    }
