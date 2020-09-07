import os
import time
from flask import Flask
app = Flask(__name__)


@app.route("/")
def main():
    return "Hello World!"

@app.route('/greet')
def hello():
    t = time.localtime()
    current_time = time.strftime("%H", t)
    if current_time == 12:
        return 'Hello its PM'
    else:
        return 'Hello its AM'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
