from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/api')
def api():
    form = request.form

    return {"result": int(form['a']) + int(form['b'])}


if __name__ == '__main__':
    app.run(debug=True, port=8000)
