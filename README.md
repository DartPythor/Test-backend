# Test-backend

Тестовое задание на Python Junior позицию.

## Начать работу

Для работы над проектом нужно его склонировать.
Перейди в свою рабочую директорию и используй эту команду:

### Скачать файлы проекта

```commandline
git clone https://github.com/DartPythor/Test-backend.git
```

### Установка Venv

Для более комфортной разработки, создай виртуальную среду:

```commandline
python -m venv venv
```

Для активации venv используй эти команды:

```commandline
For windows:
venv\Scripts\activate
For linux/MacOS:
source venv/bin/activate
```

### Зависимости

Для корректной работы проекта нужно установить зависимости:

1. Установить для прода:
    ```commandline
   pip install -r requirements/prod.txt
   ```
2. Установить для тестов:
    ```commandline
   pip install -r requirements/test.txt
   ```
3. Установить для разработки:
   ```commandline
   pip install -r requirements/dev.txt
   ```
4. Если нужно установить все:
   ```commandline
   pip install -r requirements/requirements.txt
   ```

## Создание .env

Чтобы настроить свой проект нужно использовать .env
Пример находится в example.env
Для первого раза просто скопируй его в .env файл.

```commandline
copy example.env .env
```

## Запустить dev сервер

Для запуска сервера для разработки используй эту команду:

```commandline
python manage.py runserver
```

Если все работает правильно ты получишь такое сообщение:

```commandline
Starting development server at http://127.0.0.1:8000/
```
## Запуск тестов
Если ты хочешь проверить, всё ли работает правильно
запусти тесты.

```commandline
python manage.py test
```
## Выгрузка фикстур
Если нужно выгрузить фикстуры используй команду:
```commandline
python -Xutf8 manage.py dumpdata catalog -o fixtures/data.json
```
## Загрузка фикстур
Если нужно загрузить фикстуры:
```commandline
python manage.py loaddata fixtures/data.json
```

## Contacts

Neverov Max - [Telegram](https://t.me/maximneverov)
