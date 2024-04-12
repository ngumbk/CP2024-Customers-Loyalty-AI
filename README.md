# CP2024-Customers-Loyalty-AI

## Установка
Для установки проекта требуется установить зависимости (пока что пусть
IDE подскажет).  

Также необходимо иметь локальную БД PostgreSQL, файл
cp2024_customers_loyalty/conf.py с определенными параметрами БД.  

К БД должны быть применены миграции с помощью последовательности команд:
```shell
cd cp2024_customers_loyalty
```
```shell
python manage.py migrate
```

## Запуск
Для запуска необходимо использовать в терминале команду:
```shell
python manage.py runserver
```