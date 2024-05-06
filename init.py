import argparse
import json
from core import hash_password

def initUser(token:str, password:str):
    with open("db.json", "r") as file:
        data = json.load(file)

    users = data.get("users", [])

    for user in users:
        if user.get("token") == token:
            # Encontramos al usuario con el token especificado
            user["token"] = None

            # Generar hash seguro y salt para la contraseña
            hashed_password, salt = hash_password(password)
            user["hash"] = hashed_password
            user["salt"] = salt

            update_json_file(users, "db.json")
            return "Usuario actualizado con éxito."

    return "Usuario no encontrado para el token especificado."

# Función para actualizar el archivo JSON con los nuevos datos
def update_json_file(users, filename):
    updated_data = {"users": []}

    for user in users:
        updated_data["users"].append({
            "correo_electronico": user.get("correo_electronico"),
            "token": user.get("token"),
            "hash": user.get("hash"),
            "salt": user.get("salt")
        })

    with open(filename, 'w') as file:
        json.dump(updated_data, file, indent=4)