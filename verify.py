import argparse
import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

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
        print("El token ha expirado.")
    except jwt.InvalidTokenError:
        print("Token inválido.")
    return None

def main():
    parser = argparse.ArgumentParser(description='Verifica un token bearer y muestra el contenido del JWT.')
    parser.add_argument('-t', '--token', help='Token bearer a verificar', required=True)
    args = parser.parse_args()

    clave_publica = cargar_clave_publica("public.pem")
    token_decodificado = verificar_token(args.token, clave_publica)
    if token_decodificado:
        print(token_decodificado)

if __name__ == "__main__":
    main()