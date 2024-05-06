import argparse
import json
from core import hash_password, hash_passwordSalt
import jwt

def load_users(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data.get('users', [])

def verify_credentials(email, password, users):
    for user in users:
        if user.get("correo_electronico") == email:
            stored_hash = user.get("hash")
            salt = user.get("salt")
            entered_hash = hash_passwordSalt(password, salt)
            if entered_hash == stored_hash:
                return True
    return False

def generate_token(email, password, private_key_path='private.pem'):
    with open(private_key_path, 'rb') as f:
        private_key = f.read()

    token = jwt.encode({'email': email, 'password': password}, private_key, algorithm='RS256')
    return token

def main():
    parser = argparse.ArgumentParser(description='Genera un token Bearer utilitzant JWT amb encriptació de contrasenya.')
    parser.add_argument('-e', '--email', required=True, help='Correu electrònic')
    parser.add_argument('-p', '--password', required=True, help='Contrasenya')

    args = parser.parse_args()

    users = load_users('db.json')

    if verify_credentials(args.email, args.password, users):
        token = generate_token(args.email, args.password)
        print(f'Token Bearer generat:\n{token}')
    else:
        print('Credencials no vàlides.')

if __name__ == '__main__':
    main()