import sqlite3

from telebot import types


def print_all_table(table_name: str):
    """
    Функция показывающая все столы
    :param table_name:
    :return: номер стола и кол-во мест в строку
    """
    conn = sqlite3.connect('all_restaurant_table.sql')
    cur = conn.cursor()

    cur.execute(
        f'SELECT * FROM {table_name}')
    database = cur.fetchall()

    info = ''
    for string in database:
        info += f'Номер стола: {string[1]}, кол-во мест {string[2]}\n'
    return info

    cur.close()
    conn.close()


# доделать функцию если все столики заняты выдавать
def print_free_table(restaurant: str, booking_restaurant: str) -> str:
    """
    Функция выводит в тг бот в строку все свободные столы в ресторане, принимает два параметра:

    :param restaurant: Название таблицы столов Ресторана
    :param booking_restaurant: Название таблицы зарезервированных столов в Ресторане
    :return: возвращает в строку номер стола и кол-во мест
    """
    conn = sqlite3.connect('all_restaurant_table.sql')
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM {booking_restaurant}")
    tables_booking = cur.fetchall()

    cur.execute(f"SELECT * FROM {restaurant}")
    tables_McDonald = cur.fetchall()

    number_free_table = []
    for free_table in tables_booking:
        if free_table[1] == 'True':
            number_free_table.append(free_table[0])

    info = ''
    for table in tables_McDonald:
        if table[1] in number_free_table:
            info += f'Номер стола: {table[1]}, кол-во мест {table[2]}\n'
    return info

    cur.close()
    conn.close()


def booking_tables(message) -> None:
    """
    Функция бронирует указанный номер стола
    """
    conn = sqlite3.connect('all_restaurant_table.sql')
    cur = conn.cursor()

    cur.execute(
        f"SELECT * FROM table_booking_McDonald")
    table_booking = cur.fetchall()

    for table in table_booking:
        if int(message.text) == table[0] and table[1] == 'True':
            cur.execute(
                f"UPDATE table_booking_McDonald SET booking = False WHERE number_table = {int(message.text)}")
            conn.commit()
    cur.close()
    conn.close()



# def create_database() -> None:
#     """
#     Функция добавляет в базу ресторанов, новый ресторан
#     с столбцами: id стола / номер стола / количество мест
#
#     """
#     conn = sqlite3.connect('all_restaurant_table.sql')
#     cur = conn.cursor()
#
#     cur.execute(
#         'CREATE TABLE IF NOT EXISTS table_McDonald (id int auto_increment primary key, number_table int, count_place int);')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#
# def add_table(table_name: str, number_table: int, count_place: int) -> None:
#     """
#     Функция для добавления столов в таблицу
#     :param table_McDonald: Название таблицы ресторана, в который хотим добавить столы
#     :param number_table: Номер стола
#     :param count_place: Количество мест за столом
#     """
#     conn = sqlite3.connect('all_restaurant_table.sql')
#     cur = conn.cursor()
#
#     cur.execute(
#         f'INSERT INTO {table_name} (number_table, count_place) VALUES ({number_table}, {count_place})')
#     conn.commit()
#     cur.close()
#     conn.close()

