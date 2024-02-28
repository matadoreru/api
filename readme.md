
FLASK:\n
    Inicialitza el servidor, base\n
    flask app run\n
        --app: Pots triar quin fitxer es el de l'aplicacio\n
        --debug: Activa el mode de debug\n

    
CURL:\n
    Registra a un usuari amb un token i un email\n
    curl -d "email=bustia@email.com" -X POST http://127.0.0.1:5000/api/register/\n