import json
import random
import string
longitud_bytes = 32

def generar_token(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def registerUser(email:str):
    try:
        with open('db.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {"users": []}
    
    # Verificar si el correo electrónico ya está presente
    for user in data["users"]:
        if user["correo_electronico"] == email:
            return "El correo electronico '" + email + "' ya esta registrado."

    token = generar_token(longitud_bytes)  
    user = {"correo_electronico": email, "token": token}
    data["users"].append(user)
    with open('db.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    return "Correo electronico '" + email + "' y el token '" + token + "' guardados exitosamente."