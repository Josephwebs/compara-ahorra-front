
# Instalación de dependencias por comando de Django + django rest framework + psycopg (driver postgresql)
pip install django==4.0.1 requests

# Instalación de dependencias desde un archivo (requeriments.txt)
pip install -r requeriments.txt

# Comando para crear listado de dependencias (librerias)
pip freeze > requeriments.txt

# Comando para desplegar aplicación

python manage.py runserver 9000