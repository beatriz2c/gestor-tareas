# Usamos imagen oficial de Python
FROM python:3.11-slim

# Establecemos directorio de trabajo
WORKDIR /app

# Copiamos requirements e instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la app
COPY . .

# Exponemos el puerto 5000
EXPOSE 5000

# Variable para que Flask use el app.py como entrypoint
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Ejecutamos la app
CMD ["flask", "run"]
