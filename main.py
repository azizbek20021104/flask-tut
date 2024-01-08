from flask import Flask, request


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def base():
    return "home"

@app.route('/about')
def about():
    return "about"

@app.route('/hi')
def hi():
    params = request.args
    
    return {
        "name": params['name'],
        "age": params['age'],
    }


if __name__ == '__main__':
    app.run(debug=True, port=8000)
