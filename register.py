import json
import random
import string

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
            return "El correo electrónico '" + email + "' ya está registrado."

    token = generar_token(16)  
    user = {"correo_electronico": email, "token": token}
    data["users"].append(user)
    with open('db.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    return "Correo electrónico '" + email + "' y el token '" + token + "' guardados exitosamente."