import hashlib
import secrets

def hash_password(password):
    salt = secrets.token_hex(16)
    password = password.encode('utf-8')
    salted_password = password + salt.encode('utf-8')
    hashed_password = hashlib.sha3_512(salted_password).hexdigest()
    return hashed_password, salt

def hash_passwordSalt(password, salt):
    password = password.encode('utf-8')
    salted_password = password + salt.encode('utf-8')
    hashed_password = hashlib.sha3_512(salted_password).hexdigest()
    return hashed_password