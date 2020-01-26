
Requisitos:
Sistema operativo macOS

Extraer el proyecto a una carpeta con git clone

Dirigirse a siguiente directorio:
FlaskAPI/flaskapi/

Python 3.7 instalado
Pip instalado

Instalar diferentes modulos:

pip install virtualenv

virtualenv flaskapp
pip install flask
pip install flask-sqlalchemy
pip install flask-wtf
pip install requests
pip install python
pip install virtualenv
pip install flask-migrate
pip install flask-bootstrap


flask db init
flask db migrate -m "users table"
flask db upgrade

export FLASK_APP=__init__.py
 export FLASK_ENV=development
 flask run


Dirigirse a http://localhost:5000/ y probar la api.
Al dirigirse nuevamente a la direccion dada (sin recargar), se eliminarán todos los registros ingresados.

