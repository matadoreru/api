
FLASK:
    Inicialitza el servidor, base
    flask app run
        --app: Pots triar quin fitxer es el de l'aplicacio
        --debug: Activa el mode de debug

    
CURL:
    Registra a un usuari amb un token i un email
    curl -d "email=bustia@email.com" -X POST http://127.0.0.1:5000/api/register/