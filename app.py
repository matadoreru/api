from flask import Flask, request, jsonify, render_template
from register import *
from init import *
from login import *
from verify import * 

app = Flask(__name__)


@app.route('/register')
def home():
    return render_template('register.html')

@app.route('/init')
def home():
    return render_template('init.html')

@app.route('/login')
def home():
    return render_template('login.html')

@app.route('/verify')
def home():
    return render_template('verify.html')


@app.route('/api/register/', methods=['POST'])
def register():
    print("Començar register de l'usuari")
    email = request.form.get('email')
    if not email:
        return jsonify({'error': 'El parametre "email" es obligatori.'}), 400

    return jsonify({"message": f"Usuari registrat: '{registerUser(email)}'."}), 200

@app.route('/api/init/', methods=['POST'])
def init():
    print("Inicialitzar a l'usuari")
    token = request.form.get('token')
    if not token:
        return jsonify({'error': 'El parametre "token" es obligatori.'}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({'error': 'El parametre "password" es obligatori.'}), 400

    return jsonify({"message": f"'{initUser(token, password)}'."}), 200

@app.route('/api/login/', methods=['POST'])
def login():
    print("Login usuari")
    email = request.form.get('email')
    if not email:
        return jsonify({'error': 'El parametre "email" es obligatori.'}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({'error': 'El parametre "password" es obligatori.'}), 400

    return jsonify({"message": f"'{loginUser(email, password)}'."}), 200

@app.route('/api/verify/', methods=['POST'])
def verify():
    print("Verify token")
    token = request.form.get('token')
    if not token:
        return jsonify({'error': 'El parametre "token" es obligatori.'}), 400
    return jsonify({"message": f"'{verifyToken(token)}'."}), 200


if __name__ == '__main__':
    app.run(host='192.168.1.48', port=5000, debug=True)
