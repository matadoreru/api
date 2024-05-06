from flask import Flask, request, jsonify
from register import *
from init import *
from login import *

app = Flask(__name__)

@app.route('/api/register/', methods=['POST'])
def register():
    print("Començar register de l'usuari")
    email = request.form.get('email')
    if not email:
        return jsonify({'error': 'El paràmetre "email" és obligatori.'}), 400

    return jsonify({"message": f"Usuari registrat: '{registerUser(email)}'."}), 200

@app.route('/api/init/', methods=['POST'])
def init():
    print("Inicialitzar a l'usuari")
    token = request.form.get('token')
    if not token:
        return jsonify({'error': 'El paràmetre "token" és obligatori.'}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({'error': 'El paràmetre "password" és obligatori.'}), 400

    return jsonify({"message": f"'{initUser(token, password)}'."}), 200

@app.route('/api/login/', methods=['POST'])
def login():
    print("Login usuari")
    email = request.form.get('email')
    if not email:
        return jsonify({'error': 'El paràmetre "email" és obligatori.'}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({'error': 'El paràmetre "password" és obligatori.'}), 400

    return jsonify({"message": f"'{loginUser(email, password)}'."}), 200


if __name__ == '__main__':
    app.run(host='192.168.1.48', port=5000, debug=True)
