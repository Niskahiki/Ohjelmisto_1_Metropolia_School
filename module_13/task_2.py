import mysql.connector
from mysql.connector import Error as DB_error
from mysql.connector.connection import MySQLConnectionAbstract
from flask import Flask, Response
import json

connection: MySQLConnectionAbstract
app = Flask(__name__)


def create_new_db_connection() -> None | DB_error:
    try:
        global connection

        connection = mysql.connector.connect(
            host='127.0.0.1',
            database='flight_game',
            port=3306,
            username='root',
            password='root',
            autocommit=True,
        )

        return None
    except DB_error as e:
        return e


def fetch_airport_from_db(ICAO_code: str) -> tuple | None | DB_error:

    sql = f"SELECT ident, name, municipality FROM airport WHERE ident = '{ICAO_code}'"

    cursor = connection.cursor()

    try:
        cursor.execute(sql)

        result = cursor.fetchone()

        return result
    except DB_error as e:
        return e


@app.route('/kenttä/<ICAO_code>')
def get_airport_endpoint(ICAO_code):
    try:
        airport = fetch_airport_from_db(ICAO_code)

        if airport:
            if type(airport) is DB_error:
                response_body = json.dumps({'error': 'Failed to search airport from db.', 'status': 500})
                return Response(response=response_body, status=500, mimetype='application/json')

            else:
                response_body = json.dumps({'ICAO': airport[0], 'Name': airport[1], 'Municipality': airport[2]})
                return Response(response=response_body, status=200, mimetype='application/json')

        else:
            response_body = json.dumps({'error': 'No airport found with the given ICAO code.', 'status': 400})
            return Response(response=response_body, status=400, mimetype='application/json')

    except IndexError as e:
        response_body = json.dumps({'error': 'Some data from airport was missing.', 'status': 500})
        return Response(response=response_body, status=500, mimetype='application/json')


if __name__ == "__main__":
    err = create_new_db_connection()

    if not err:
        print("Database connection established.")
        app.run(host='127.0.0.1', port=3000, use_reloader=True)
    else:
        print(f"Error occurred while trying to connect to the database. Error: {err}")
