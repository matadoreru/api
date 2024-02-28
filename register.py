import json
import secrets

longitud_bytes = 32

def generar_token(longitud):
    token_bytes = secrets.token_bytes(longitud_bytes)
    return secrets.token_hex(longitud_bytes)

def registerUser(email:str):
    try:
        with open('db.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {"users": []}
    
    token = generar_token(longitud_bytes)
    user = {"correo_electronico": email, "token": token}
    data["users"].append(user)
    with open('db.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Se ha registrado el usuario con el correo electrónico '{email}' y el token '{token}'.")