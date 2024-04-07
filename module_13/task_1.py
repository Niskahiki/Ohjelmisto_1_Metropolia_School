from flask import Flask, Response
import json


app = Flask(__name__)


def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False

        if i == num - 1:
            return True

    return True  # if value is 2 or 1


@app.route('/alkuluku/<number>')
def is_prime_endpoint(number):
    try:
        number = int(number)

        is_number_prime = is_prime(number)

        response_body = json.dumps({'Number': number, 'isPrime': is_number_prime})

        return Response(response=response_body, status=200, mimetype='application/json')
    except ValueError as e:
        response_body = json.dumps({'error': 'Provided value was not int.', 'status': 400})
        return Response(response=response_body, status=400, mimetype='application/json')


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)
