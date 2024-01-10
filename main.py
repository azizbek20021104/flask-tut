from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/api')
def api():
    data = json.loads(request.data.decode())

    return {"result": data['a'] + data['b']}


if __name__ == '__main__':
    app.run(debug=True)
