import pytest

import data
import sender_stand_request


@pytest.fixture
def order_track():
    """
    Подготовка: создаёт заказ и возвращает его трек.
    Это не проверка, а setup для теста получения по треку.
    """
    response = sender_stand_request.post_new_order(data.order_body)
    assert response.status_code == 201, (
        f"Не удалось создать заказ для подготовки теста: "
        f"{response.status_code} {response.text}"
    )
    return response.json()["track"]


def test_create_order_returns_201():
    """Одно состояние: создание заказа возвращает код 201."""
    response = sender_stand_request.post_new_order(data.order_body)
    assert response.status_code == 201


def test_get_order_by_track_returns_200(order_track):
    """Одно состояние: получение заказа по треку возвращает код 200."""
    response = sender_stand_request.get_order_by_track(order_track)
    assert response.status_code == 200
