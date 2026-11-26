import requests

import configuration
import data


def post_new_order(body):
    """
    Создаёт заказ и возвращает объект ответа.
    В теле успешного ответа содержится номер трека заказа.
    """
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
        headers=data.headers
    )


def get_order_by_track(track):
    """
    Получает заказ по номеру трека.
    Трек передаётся query-параметром t.
    """
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        params={"t": track},
        headers=data.headers
    )
