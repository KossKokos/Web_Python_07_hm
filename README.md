1) В папці "src" є файл "db.py" в якому я зєднав нашу базу і створив session.
2) Також там є файл "models" в якому я створив таблиці та поєднав їх.
3) В папці "seed" є файл "insert_into_tables.py" в якому я заповнюю дані в таблиці, використовуючи "faker".
4) В файлі "my_select.py" є функції, які дістають дані з різних таблиць та об'єднують їх.
5) Файл "main.py" - це  CLI програма для CRUD операцій із базою даних.
6) В папці "crud" реалізовано 4 файли: "create_models", "list_models", "remove_models", "update_models", які реалізують конкретні функції для crud операцій.
7) Requirements:
    1) alembic
    2) faker
    3) psycopg2
    4) SQLAlchemy