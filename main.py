from flask import Flask, request


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def base():
    return "home"

@app.route('/about')
def about():
    return "about"

@app.route('/hi', mehtods=['GET', 'POST'])
def hi():
    if request.method == 'GET':
        params = request.args
        
        return {
            "name": params['name'],
            "age": params['age'],
        }
    else:
        return {"error": "method nor allowed."}


if __name__ == '__main__':
    app.run(debug=True, port=8000)
