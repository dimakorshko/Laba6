import Connection
from prettytable import PrettyTable

try:
    # Подключение к базе данных
    connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
    cursor = connection.cursor()

    def print_table(name_table):
        cursor.execute("SELECT * FROM " + name_table)
        data = cursor.fetchall()
        table = PrettyTable()
        table.field_names = [description[0] for description in cursor.description]
        for row in data:
            table.add_row(row)
        print(table)

    print_table("Locomotives")
    print_table("Brigades")
    print_table("Workers")
    print_table("Repairs")

except Exception as e:
    print(f"Помилка при виводі таблиць в консоль: {e}")

finally:
    # Закрытие соединения
    cursor.close()
    connection.close()
