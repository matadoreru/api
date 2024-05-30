# Utilitza una imatge base oficial de Python
FROM python:3.9-slim

# Crea un directori de treball anomenat "app"
WORKDIR /app

# Copia el fitxer requirements.txt al directori de treball
COPY requeriments.txt .

# Instal·la les dependències necessàries
RUN pip3 install -r requeriments.txt

# Copia el contingut de la carpeta "flask" al directori de treball "app"
COPY flask/ .

# Exposa el port 5000 del contenidor
EXPOSE 5000

# Crea un volum per contenir el fitxer "db.json"
VOLUME /app/db

# Estableix la variable d'entorn necessària per executar Flask
ENV FLASK_APP=app.py

# Executa la comanda per iniciar l'aplicació Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
