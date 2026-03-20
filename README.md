📚 Домашняя библиотека — REST API

REST API для управления списком книг.
Приложение позволяет:

* ➕ Добавлять книги

* 📖 Получать список всех книг

* 🔍 Искать конкретную книгу

* ✏️ Обновлять данные книги

* 🗑 Удалять книги


🗂 Структура проекта
my_library/
├── main.py              # 🚀 Запуск приложения, подключение роутеров
├── database.py          # 🛠 Настройка движка (Engine) и сессий
├── models/              # 🏗 SQLAlchemy модели (таблицы)
│   └── books.py
├── schemas/             # 📐 Pydantic схемы (валидация)
│   └── books.py
├── routers/             # 🌐 Эндпоинты (HTTP-логика)
│   └── books.py
├── repository/          # 💾 Логика работы с БД (SQL-запросы)
│   └── books.py


📝 Модель данных (База данных)
    Поле	Тип SQL	Тип Python	Описание
    id	INTEGER	int	🔑 Первичный ключ (Primary Key)
    title	VARCHAR	str	📖 Название книги (не может быть пустым)
    author	VARCHAR	str	✍️ Автор книги (не может быть пустым)
    year	INTEGER	int	🗓 Год издания
    pages	INTEGER	int	📄 Количество страниц (минимум 10)
    is_read	BOOLEAN	bool	✅ Прочитана ли книга (по умолчанию False)

    
📦 Схемы данных (Pydantic)
    1) SBookAdd — создание/обновление книги
    
    Поля: title, author, year, pages, is_read
    
    Все поля обязательны, кроме is_read (по умолчанию False)
    
    Валидация: pages > 10

    2) SBook — возвращаемый объект
    
    Все поля из SBookAdd + id
    
    Настройка: from_attributes = True

🌐 API Эндпоинты

Все методы используют Dependency Injection для получения сессии БД и Repository для работы с SQL.

    🔹 Метод	URL	Описание	Вход	Выход	Статус
    POST	/books	➕ Добавить книгу	JSON (SBookAdd)	JSON (SBook)	201 Created
    GET	/books	📖 Получить все книги	—	Список JSON (list[SBook])	200 OK
    GET	/books/{id}	🔍 Получить одну книгу	ID книги (int)	JSON (SBook)	200 OK / 404 Not Found
    PUT	/books/{id}	✏️ Полное обновление книги	ID + JSON (SBookAdd)	JSON (SBook)	200 OK / 404 Not Found
    DELETE	/books/{id}	🗑 Удалить книгу	ID книги	Пусто	204 No Content / 404 Not Found


🔧 Примеры запросов
Добавление книги
    curl -X POST http://localhost:8000/books \
    -H "Content-Type: application/json" \
    -d '{"title":"Война и мир","author":"Л.Н. Толстой","year":1869,"pages":1225}'
    
Получение всех книг
    curl http://localhost:8000/books
    
Получение книги по ID
    curl http://localhost:8000/books/1
    
Обновление книги
    curl -X PUT http://localhost:8000/books/1 \
    -H "Content-Type: application/json" \
    -d '{"title":"Война и мир","author":"Л.Н. Толстой","year":1869,"pages":1230}'

Удаление книги
    curl -X DELETE http://localhost:8000/books/1

    
🛠 Технологии:

* Python 3.12+

* FastAPI

* SQLAlchemy (async)

* Pydantic

* SQLite (библиотека aiosqlite)
