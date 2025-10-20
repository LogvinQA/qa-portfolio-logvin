# 🧩 Учебный проект QA — Rasul Logvin

Этот репозиторий — портфолио начинающего тестировщика **Расула Логвина**.  
Здесь собраны тест-кейсы, коллекции Postman и баг-репорты, выполненные в рамках учебных проектов.

---

## 📁 Состав репозитория

| Раздел | Содержание |
|--------|-------------|
| [`docs/test-cases.xlsx`](./docs/test-cases.xlsx) | 10 тест-кейсов для сайта [saucedemo.com](https://www.saucedemo.com) (позитивные, негативные, граничные значения) |
| [`postman/saucedemo_collection.json`](./postman/saucedemo_collection.json) | Коллекция запросов с тестами API (GET/POST/PUT/DELETE, проверка статусов и структуры JSON) |
| `README.md` | Описание проекта и инструкция по запуску |

---

## 🧠 Инструменты

- **Jira (Kanban)** — ведение баг-репортов и задач  
- **Postman** — ручное тестирование API  
- **Chrome DevTools** — исследование UI, сетевых запросов и консоли  
- **GitHub** — хранение тестовой документации  
- **OC:** macOS  
- **Браузер:** Chrome 139.0  

---

## 🚀 Как воспроизвести

1. Перейти на сайт [saucedemo.com](https://www.saucedemo.com)  
2. Логин: `standard_user`, пароль: `secret_sauce`  
3. Использовать тест-кейсы из `docs/test-cases.xlsx`  
4. Импортировать коллекцию Postman и запустить тесты  

---

## 🧩 Примеры баг-репортов

| Тип | Описание |
|------|-----------|
| **UI** | Текст ошибки выходит за границы блока при неверном логине/пароле |
| **Functional** | Поле email принимает значения без символа `@` |
| **API** | Эндпоинт возвращает `404` вместо ожидаемого `200` (пример с jsonplaceholder) |

---

## 📸 Скриншоты API-тестов Postman

| Метод | Скриншот |
|--------|-----------|
| **GET** | ![GET test](./screenshots/postman/get_test_1.png) |
| **POST** | ![POST test](./screenshots/postman/get_test_2.png) |
| **PUT** | ![PUT test](./screenshots/postman/get_test_3.png) |
| **DELETE** | ![DELETE test](./screenshots/postman/get_test_4.png) |

> Каждый тест проверяет корректность структуры, статус-коды и формат ответа (JSON).  
> Тесты выполнены в **Postman**, с использованием встроенного JavaScript-валидационного движка.

---

## 👤 Автор

**Расул Логвин**  
QA Trainee — 2025  

📌 Инструменты: Jira · Postman · Chrome DevTools · GitHub  
📬 Контакты: [Telegram](https://t.me/pando_s)
