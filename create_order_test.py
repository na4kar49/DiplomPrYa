import data
import sender_stand_request


def test_create_and_get_order_by_track():
    """
    Проверяет, что по треку созданного заказа можно получить данные заказа.

    Шаги:
    1. Отправить запрос на создание заказа.
    2. Сохранить номер трека заказа.
    3. Отправить запрос на получение заказа по треку.
    4. Проверить, что код ответа равен 200.
    """
    # Шаг 1. Создание заказа
    create_response = sender_stand_request.post_new_order(data.order_body)

    # Шаг 2. Сохранение трека (в ответе на создание заказа приходит track)
    assert create_response.status_code == 201, (
        f"Ожидался код 201 при создании заказа, получен {create_response.status_code}. "
        f"Ответ: {create_response.text}"
    )
    track = create_response.json()["track"]
    assert track, "В ответе на создание заказа отсутствует поле track"

    # Шаг 3. Получение заказа по треку
    get_response = sender_stand_request.get_order_by_track(track)

    # Шаг 4. Проверка кода ответа
    assert get_response.status_code == 200, (
        f"Ожидался код 200 при получении заказа по треку, получен {get_response.status_code}. "
        f"Ответ: {get_response.text}"
    )
