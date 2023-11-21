import Connection

connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
cursor = connection.cursor()

def run_query(sql_query):
    # Подключение к базе данных и выполнение запроса
    try:
        cursor.execute(sql_query)

        # Получение результатов запроса
        records = cursor.fetchall()

        # Вывод результатов
        for record in records:
            print(record)

    except Exception as e:
        print(f"Ошибка: {e}")

# Запит 1
# -------------------------------------------------------------------
print("Відобразити всі локомотиви, які мають тип вантажний. Відсортувати за роком випуску" )
sql_query = """
    SELECT *
    FROM Locomotives
    WHERE type = 'вантажний'
    ORDER BY year_of_production ASC;
"""
run_query(sql_query)

#Запит 2
#------------------------------------------------------------
print("Порахувати кінцеву дату ремонту для кожного локомотива")
sql_query = """
    SELECT
        registration_number,
        to_char(MAX(date_of_start + day_until_the_end * INTERVAL '1 day'), 'YYYY-MM-DD') AS end_date_of_repair
        
    FROM
        Repairs
    GROUP BY
        registration_number
    ORDER BY registration_number;

"""
run_query(sql_query)

# Запит 3
# ------------------------------------------------------------
print("Порахувати кількість ремонтів, які виконала кожна бригада:")
sql_query = """
       SELECT
        b.brigade_number,
        COUNT(r.repair_id) AS repairs_count
    FROM
        Brigades b
    JOIN
        Repairs r ON b.brigade_number = r.brigade_number
    GROUP BY
        b.brigade_number
    ORDER BY b.brigade_number;
"""
run_query(sql_query)

# Запит 4
# ------------------------------------------------------------
print("Порахувати повну вартість ремонту для кожного локомотива, який було відремонтовано:")
sql_query = """
    SELECT
        registration_number,
        to_char(SUM(CAST(repair_cost AS INT) * GREATEST(EXTRACT(DAY FROM AGE(CURRENT_DATE, date_of_start)) + day_until_the_end, 0)), 'FM999999999') AS total_repair_cost
    FROM
        Repairs
    WHERE
        date_of_start + day_until_the_end * INTERVAL '1 day' <= CURRENT_DATE
    GROUP BY
        registration_number
    ORDER BY registration_number;
"""
run_query(sql_query)

# Запит 5
# ------------------------------------------------------------
print("Порахувати кількість типів ремонтів, які виконала кожна бригада:")
sql_query = """
    SELECT
        b.brigade_number,
        r.type_of_repair,
        COUNT(r.type_of_repair) AS repair_type_count
    FROM
        Brigades b
    CROSS JOIN
        Repairs r
    WHERE
        b.brigade_number = r.brigade_number
    GROUP BY
        b.brigade_number, r.type_of_repair
    ORDER BY brigade_number;

"""
run_query(sql_query)

# Запит 6
# ------------------------------------------------------------
print("Відобразити всіх локомотиви, які приписані до обраного депо:")

sql_query = """
    SELECT
        *
    FROM
        Locomotives
    WHERE
        registration_place = 'Козятин';

"""
run_query(sql_query)


# Закриття підключення
cursor.close()
connection.close()