# 🧩 Учебный проект QA — Rasul

Этот репозиторий — портфолио начинающего тестировщика ** Логвина Расула**.  
Здесь собраны тест-кейсы, коллекции Postman и баг-репорты, выполненные в рамках учебных проектов.

---

## 📂 Состав репозитория

| Раздел | Содержание |
|--------|-------------|
| [`docs/test-cases.xlsx`](docs/test-cases.xlsx) | 10 тест-кейсов для сайта [saucedemo.com](https://www.saucedemo.com) (позитивные, негативные, граничные значения) |
| [`postman/saucedemo_collection.json`](postman/saucedemo_collection.json) | Коллекция запросов с тестами API (GET/POST, проверки статуса 200 и JSON) |
| `README.md` | Описание проекта и инструкция для запуска |

---

## 🧠 Инструменты

- **Jira (Kanban)** — создание и ведение баг-репортов  
- **Postman** — ручное тестирование API  
- **Chrome DevTools** — исследование UI, сетевых запросов и консоли  
- **GitHub** — контроль версий, хранение тестовой документации  
- **ОС:** macOS  
- **Браузер:** Chrome 139.0  

---

## 🚀 Как воспроизводить

1. Перейти на сайт [https://www.saucedemo.com/](https://www.saucedemo.com)  
2. Ввести логин: `standard_user` и пароль: `secret_sauce`  
3. Использовать тест-кейсы из `docs/test-cases.xlsx`  
4. Импортировать коллекцию Postman и запустить тесты  

---

## 🐞 Примеры баг-репортов

| Тип | Описание |
|-----|-----------|
| **UI** | Текст ошибки выходит за границы блока при неверном логине/пароле |
| **Functional** | Поле email принимает значения без символа `@` |
| **API** | Эндпоинт возвращает 404 вместо ожидаемого 200 (пример с jsonplaceholder) |

---

## 📸 Скриншоты проекта (опционально)
## 🧪 Результаты API-тестов Postman

| Метод | Проверка | Результат |
|-------|-----------|------------|
| **GET** | Проверка структуры и статуса 200 | ✅ |
| **POST** | Создание нового поста | ✅ |
| **PUT** | Обновление данных поста | ✅ |
| **DELETE** | Удаление поста | ✅ |

### Скриншоты тестов
GET:
![GET test](screenshots/postman/get_test.png)

POST:
![POST test](screenshots/postman/get_test1.png)

PUT:
![PUT test](screenshots/postman/get_test2.png)

DELETE:
![DELETE test](screenshots/postman/get_test3.png)

---

## 👤 Автор

**Расул Логвин**  
QA Trainee — 2025  
📍 Инструменты: Jira · Postman · Chrome DevTools · GitHub  
📬 Контакты: (https://t.me/pando_s)

---
