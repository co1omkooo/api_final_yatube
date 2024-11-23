### Описание проекта

Проект API для Yatube представляет собой API для управления постами, комментариями, группами постов и подписками. 

### Технологии

В проекте использовались: python, Django, Django Rest Framework, djoser, JWT, pytest, redoc.

### Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/co1omkooo/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

* Если у вас Linux/macOS

    ```
    python3 -m venv env
    source env/bin/activate
    ```

* Если у вас Windows

    ```
    python -m venv env
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Документация

Документация API и примеры запросов доступны по адресу http://127.0.0.1:8000/redoc/ после запуска локального сервера по инструкции выше.
