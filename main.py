from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola, mundo! Este es un servidor web sencillo con Flask en Python.'

if __name__ == '__main__':
    app.run(debug=True)