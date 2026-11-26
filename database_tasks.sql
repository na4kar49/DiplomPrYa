-- Задание 1. Логины курьеров и количество заказов «В доставке»
SELECT
    c.login,
    COUNT(o.id) AS orders_in_delivery
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o
    ON o."courierId" = c.id
   AND o."inDelivery" = true
GROUP BY c.login
ORDER BY orders_in_delivery DESC, c.login;

-- Задание 2. Трекеры заказов и их статусы
SELECT
    track,
    CASE
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS status
FROM "Orders"
ORDER BY track;
