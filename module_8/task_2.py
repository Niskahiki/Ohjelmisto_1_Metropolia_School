import mysql.connector
from mysql.connector.cursor import MySQLCursorAbstract


def get_country_airport_types_from_db_by_country_code(cursor: MySQLCursorAbstract, country_code) -> dict or None:
    sql = f"SELECT type FROM airport WHERE iso_country = '{country_code}'"
    cursor.execute(sql)

    result = cursor.fetchall()
    if not result or len(result) == 0:
        return None

    type_set = set()
    airport_type_count_dict = {}

    # Get different airport types from the result list
    for type_value in result:
        type_set.add(type_value[0])

    # Get count of every type in the result list
    for airport_type in type_set:
        type_count = 0
        result_copy = result.copy()
        for type_value in result_copy:
            if type_value[0] == airport_type:
                type_count += 1
                result.remove(type_value)

        airport_type_count_dict[airport_type] = type_count

    return airport_type_count_dict


def main():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database="flight_game",
        user="<USERNAME>",
        password="<PASSWORD>",
        autocommit=True
    )

    country_code = input("Anna maakoodi: ")

    cursor = connection.cursor()
    airport_types = get_country_airport_types_from_db_by_country_code(cursor, country_code)

    if airport_types:
        for value in airport_types:
            print(value, airport_types[value])
    else:
        print("Lentokenttiä ei löydetty.")


if __name__ == "__main__":
    main()
