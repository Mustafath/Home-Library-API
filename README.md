# 📚 Home Library API

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-black?logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-Async-orange?logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![SQLite](https://img.shields.io/badge/Database-SQLite-green?logo=sqlite)](https://sqlite.org/)

**REST API для управления домашней библиотекой книг.** Полный CRUD с валидацией, асинхронной БД и автодокументацией.

## ✨ Возможности

| ➕ | **Создание** книг с валидацией |
|---|-------------------------------|
| 📖 | **Чтение** всех книг или по ID |
| ✏️ | **Обновление** данных книги   |
| 🗑 | **Удаление** книг            |
| 🔍 | **Автодокументация** Swagger/ReDoc |


## 🗂 Структура проекта
```
Home-Library-API/
├── my_library/
│ ├── main.py # 🚀 Точка входа FastAPI
│ ├── database.py # 🛠 Engine и сессии БД
│ ├── models/
│ │ └── books.py # 🏗 SQLAlchemy модели
│ ├── schemas/
│ │ └── books.py # 📐 Pydantic схемы
│ ├── routers/
│ │ └── books.py # 🌐 API роуты
│ └── repository/
│ └── books.py # 💾 Репозиторий паттерны
└── README.md
```

---

## 📋 Модель БД (SQLite)

| Поле     | Тип      | Описание                  |
|----------|----------|---------------------------|
| `id`     | `int`    | 🔑 **Primary Key**        |
| `title`  | `str`    | 📖 **Название** (req)     |
| `author` | `str`    | ✍️ **Автор** (req)        |
| `year`   | `int`    | 🗓 **Год**                |
| `pages`  | `int`    | 📄 **Страницы** (>10)     |
| `is_read`| `bool`   | ✅ **Прочитано** (def: F) |


## 🌐 API Эндпоинты

| Метод | Endpoint       | Описание       | Статус    |
|-------|----------------|----------------|-----------|
| `POST`| `/books/`      | ➕ Создать     | `201`     |
| `GET` | `/books/`      | 📖 Все книги  | `200`     |
| `GET` | `/books/{id}`  | 🔍 По ID      | `200/404` |
| `PUT` | `/books/{id}`  | ✏️ Обновить   | `200/404` |
| `DEL` | `/books/{id}`  | 🗑 Удалить    | `204/404` |

---

## 🚀 Быстрый старт

### 1. Клонирование
```bash
git clone https://github.com/Mustafath/Home-Library-API.git
cd Home-Library-API/my_library
```

2. Установка
```bash
pip install fastapi uvicorn sqlalchemy aiosqlite pydantic
```

3. Запуск
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

4. Документация
Swagger: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

🧪 Примеры запросов
➕ Добавить книгу
``` bash
curl -X POST "http://localhost:8000/books/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Война и мир",
    "author": "Л.Н. Толстой",
    "year": 1869,
    "pages": 1225,
    "is_read": false
  }'
```

📖 Все книги
```bash
curl "http://localhost:8000/books/"
```

🔍 Книга по ID
```bash
curl "http://localhost:8000/books/1"
```

✏️ Обновить
```bash
curl -X PUT "http://localhost:8000/books/1" \
  -H "Content-Type: application/json" \
  -d '{"title":"Война и мир (обновлено)","pages":1230,"is_read":true}'
```

🗑 Удалить
```bash
curl -X DELETE "http://localhost:8000/books/1"
```

---

### 🛠 Технологии
*FastAPI — API фреймворк*

*SQLAlchemy (async) — ORM*

*Pydantic — валидация данных*

*SQLite (aiosqlite) — БД*

*Python 3.12+*

---

### 📁 Репозиторий паттерн

*Repository → SQLAlchemy queries*

*Router → HTTP логика - endpoints (Dependency Injection)*

*Schemas → Валидация (Pydantic)* 

*Models → БД таблицы*

---

### 🤝 Contributing
Fork проекта

*Создай feature branch (git checkout -b feature/AmazingFeature)*

*Commit изменения (git commit -m 'Add some AmazingFeature')*

*Push (git push origin feature/AmazingFeature)*

*Открой Pull Request*

---

### 📄 Лицензия
MIT — свободное использование!

* ⭐ Star проект если понравилось!
* 🐛 Issues/PRs welcome
* 📞 Связаться: Mustafath GitHub
