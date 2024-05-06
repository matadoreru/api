from flask import Flask, request, jsonify
from register import *
app = Flask(__name__)

@app.route('/api/register/', methods=['POST'])
def register():
    print("Començar register de l'usuari")
    email = request.form.get('email')
    if not email:
        return jsonify({'error': 'El paràmetre "email" és obligatori.'}), 400
    registerUser(email)

    return jsonify({"message": f"Usuari registrat amb l'email '{email}'."}), 200


if __name__ == '__main__':
    app.run(host='192.168.1.48', port=5000, debug=True)
