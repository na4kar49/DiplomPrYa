headers = {
    "Content-Type": "application/json"
}

# Тело запроса на создание заказа.
# Поля соответствуют требованиям API Яндекс.Самоката.
order_body = {
    "firstName": "Тест",
    "lastName": "Тестов",
    "address": "Москва, ул. Тестовая, д. 1",
    "metroStation": 4,
    "phone": "+79998887766",
    "rentTime": 5,
    "deliveryDate": "2026-11-20",
    "comment": "Тестовый заказ для автотеста",
    "color": ["BLACK"]
}
