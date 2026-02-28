# REST API Service

REST API на FastAPI с CRUD операциями.

## Запуск
```
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoints
- GET /items - Список всех элементов
- POST /items - Создать элемент
- GET /items/{id} - Получить элемент
- PUT /items/{id} - Обновить элемент
- DELETE /items/{id} - Удалить элемент


## Как запустить

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск
python main.py
```

## Структура проекта

```
.
├── main.py          # Точка входа
├── requirements.txt # Зависимости
└── README.md        # Этот файл
```

## Автор

Создано с помощью Genesis AI 🤖
