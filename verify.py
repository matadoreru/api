import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def verifyToken(token:str):
    clave_publica = cargar_clave_publica("public.pem")
    token_decodificado = verificar_token(token, clave_publica)
    if token_decodificado:
        return "Token decodificado: " + str(token_decodificado)

def cargar_clave_publica(archivo_clave_publica):
    with open(archivo_clave_publica, 'rb') as f:
        clave_publica = serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )
    return clave_publica

def verificar_token(token_bearer, clave_publica):
    try:
        token_decodificado = jwt.decode(token_bearer, clave_publica, algorithms=['RS256'])
        return token_decodificado
    except jwt.ExpiredSignatureError:
        return "El token ha expirado."
    except jwt.InvalidTokenError:
        return "Token invalido."
    return None