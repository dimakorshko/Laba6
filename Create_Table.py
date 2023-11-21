import Connection

# Подключение к базе данных
connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
cursor = connection.cursor()

try:
    # Создание таблицы локомотивов
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Locomotives (
        registration_number integer PRIMARY KEY,
        registration_place varchar(255),
        type varchar(20),
        year_of_production integer
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Locomotives: {e}")

try:
    # Создание таблицы бригад
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Brigades (
        brigade_number integer PRIMARY KEY,
        phone_number varchar(13)
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Brigades: {e}")

try:
    # Создание таблицы ремонта
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Repairs (
        repair_id serial PRIMARY KEY,
        registration_number integer,
        type_of_repair varchar(255),
        date_of_start DATE,
        day_until_the_end integer,
        repair_cost integer,
        brigade_number integer,
        FOREIGN KEY (registration_number) REFERENCES Locomotives(registration_number),
        FOREIGN KEY (brigade_number) REFERENCES Brigades(brigade_number)
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Repairs: {e}")

try:
    # Создание таблицы работников
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Workers (
        worker_id serial PRIMARY KEY,
        surname varchar(255),
        name varchar(255),
        patronymic varchar(255),
        brigade_number integer,
        is_brigadier BOOLEAN,
        birth_date DATE,
        FOREIGN KEY (brigade_number) REFERENCES Brigades(brigade_number)
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Workers: {e}")

    cursor.close()
    connection.close()
