# Приложение для управления пользователями и кошельками

Этот проект представляет собой API для управления пользователями и их кошельками. Используя Django и Django REST Framework, он позволяет создавать, обновлять и управлять пользователями и их балансами.

## Установка

1. Клонируйте репозиторий:

   ```
   git clone https://github.com/EgorIvanov96/wallet.git
   cd ваш_репозиторий
   ```

2. Создайте и активируйте виртуальное окружение:

   ```
   python -m venv venv
   source venv/bin/activate  # на Windows используйте venv\Scripts\activate
   ```

3. Установите необходимые зависимости:

   ```
   pip install -r requirements.txt
   ```

4. Выполните миграции базы данных:

   ```
   python manage.py migrate
   ```

5. Создайте суперпользователя, чтобы получить доступ к админке:

   ```
   python manage.py createsuperuser
   ```


## Запуск

Запустите сервер разработки:

```
python manage.py runserver
```

## Запуск через docker-compose.yml

1. Установите Docker

2. Перейдите в папку с проектом

3. Создайте файл .env в корне проекта

```bash
POSTGRES_USER=Имя пользователя для подключения к базе данных.
```

```bash
POSTGRES_PASSWORD=Пароль для подключения к базе данных PostgreSQL.
```

```bash
POSTGRES_DB=Имя базы данных PostgreSQL, с которой вы хотите подключиться.
```

```bash
DB_HOST=Хост базы данных PostgreSQL. В данном случае, значение должно быть 'db'.
```

```bash
DB_PORT=Порт, на котором работает база данных PostgreSQL. В данном случае, значение должно быть '5432'
```

```bash
SECRET_KEY= Секретный ключ, используемый для аутентификации и безопасности вашего приложения.
```

```bash
ALLOWED_HOSTS=Список хостов, которые можно разрешить для доступа к вашему приложению. Вы можете указать конкретные имена хостов, разделяя их запятыми.
```

4. Запустите файл docker-compose.yml

```
   docker compose up --build
   ```

5. Соберите статику Django

```
   docker compose exec backend python manage.py collectstatic
   ```

6. Теперь из этой директории копируем статику в /backend_static/static/

```
   docker compose exec backend cp -r /app/collected_static/. /backend_static/static/ 
   ```
7. Приложение ГОТОВО к работе

Теперь вы можете получить доступ к API по адресу `http://localhost:8000/api/v1/`.

## Использование API

### Регистрация пользователя

- **POST** `/api/v1/users/`
- Данные:
  ```json
  {
    "email": "example@example.com",
    "username": "your_username"
  }
  ```

### Просмотр пользователей

- **GET** `/api/v1/users/`

### Создание кошелька

- **POST** `/api/v1/wallets/`

### Операции с кошельком

- **POST** `/api/v1/wallets/{WALLET_UUID}/operation/`
- Данные:
  ```json
  {
    "operationType": "DEPOSIT",  // или "WITHDRAW"
    "amount": 100.0              // сумма для операции
  }
  ```
