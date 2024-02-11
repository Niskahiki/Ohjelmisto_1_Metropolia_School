import mysql.connector
from mysql.connector.cursor import MySQLCursorAbstract


def get_airport_name_and_municipality_from_db_by_code(cursor: MySQLCursorAbstract, airport_code):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{airport_code}'"
    cursor.execute(sql)
    return cursor.fetchone()


def main():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user="<USERNAME>",
        password="<PASSWORD>",
        autocommit=True
    )

    usr_airport_code = input("Anna lentokentän ICAO-koodi: ")

    cursor = connection.cursor()
    airport = get_airport_name_and_municipality_from_db_by_code(cursor, usr_airport_code)

    if airport:
        print(f"Nimi: {airport[0]}, sijaintikunta: {airport[1]}.")
    else:
        print("Lentokenttää ei löydetty")


if __name__ == "__main__":
    main()
