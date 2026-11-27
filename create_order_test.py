import data
import sender_stand_request


def test_get_order_by_track_returns_200():
    # Шаг 1. Выполнить запрос на создание заказа
    create_response = sender_stand_request.post_new_order(data.order_body)

    # Шаг 2. Сохранить номер трека заказа
    track = create_response.json()["track"]

    # Шаг 3. Выполнить запрос на получение заказа по треку
    get_response = sender_stand_request.get_order_by_track(track)

    # Шаг 4. Проверить, что код ответа равен 200
    assert get_response.status_code == 200, (
        f"Ожидался 200, получен {get_response.status_code}. "
        f"Тело: {get_response.text}"
    )
