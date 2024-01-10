from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/api')
def api():
    data = request.json

    return {"result": data['a'] + data['b']}


if __name__ == '__main__':
    app.run(debug=True, port=8000)
