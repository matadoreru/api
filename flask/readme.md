# Guía de Uso

## Flask

### Inicialización del Servidor Flask

Para inicializar el servidor Flask, ejecuta el siguiente comando en tu terminal:

```bash
flask run
```

#### Opciones:

- `--app`: Permite elegir el archivo de la aplicación.
- `--debug`: Activa el modo de depuración.

### CURL

Para registrar un usuario con un token y un correo electrónico, utiliza el siguiente comando CURL en tu terminal:

```bash
curl -d "email=tucorreo@email.com" -X POST http://127.0.0.1:5000/api/register/
```