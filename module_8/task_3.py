import mysql.connector
from mysql.connector.cursor import MySQLCursorAbstract
from geopy import distance


def get_airport_location_from_database(cursor: MySQLCursorAbstract, airport_code: str) -> tuple or None:
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{airport_code}'"
    cursor.execute(sql)
    result = cursor.fetchone()

    return result


def count_distance_between_two_locations(location1: tuple, location2: tuple) -> float:
    distance_between = distance.distance(location1, location2).km

    return distance_between


def main():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='<USERNAME>',
        password='<PASSWORD>',
        autocommit=True
    )

    cursor = connection.cursor()

    airport_1 = input("Anna ensimmäinen ICAO-koodi: ")
    airport_2 = input("Anna toinen ICAO-koodi: ")

    location_1 = get_airport_location_from_database(cursor, airport_1)
    location_2 = get_airport_location_from_database(cursor, airport_2)

    if not location_1:
        print("Ensimmäisen ICAO-koodin omaavaa lentokenttää tai sen sijainti tietoja ei löydetty.")
    elif not location_2:
        print("Toisen ICAO-koodin omaavaa lentokenttää tai sen sijainti tietoja ei löydetty.")
    else:
        distance_between = count_distance_between_two_locations(location_1, location_2)
        print(f"Kahden annetun lentokentän välinen etäisyys on: {distance_between}km")


if __name__ == "__main__":
    main()
