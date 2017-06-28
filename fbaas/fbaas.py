
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/fizz/<num>')
def api_fizz(num):
    num = int(num)
    if num not in range(1,501):
        return jsonify(error="Out of bounds"), 400
    elif num%3 != 0:
        return jsonify(error="Not divisible by 3"), 404
    elif num%3 == 0:
        return jsonify(value="Fizz")

@app.route('/buzz/<num>')
def api_buzz(num):
    num = int(num)
    if num not in range(1,501):
        return jsonify(error="Out of bounds"), 400
    elif num%5 != 0:
        return jsonify(error="Not divisible by 5"), 404
    elif num%5 == 0:
        return jsonify(value="Buzz")

@app.route('/fizzbuzz/<num>')
def api_fizzbuzz(num):
    num = int(num)
    if num not in range(1,1001):
        return jsonify(error="Out of bounds"), 400
    elif num%5 != 0 and num%3 != 0:
        return jsonify(error="Not divisible by 3 or 5"), 404
    elif num%5 == 0 and num%3 == 0:
        return jsonify(value="FizzBuzz")
    elif num%5 == 0:
        return jsonify(value="Buzz")
    elif num%3 == 0:
        return jsonify(value="Fizz")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

