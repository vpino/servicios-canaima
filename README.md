===============================
Instalacion de la base de datos

Primero es necesario instalar los siguientes paquetes:

- postgresql-9.4
- postgresql-server-dev-9.4

Luego se configura la base de datos logeando como el usuario postgres:

su postgres

Una vez en la consola de postgres se ejecutan los siguientes comandos:

DROP DATABASE IF EXISTS canaima;
DROP ROLE IF EXISTS canaima;
CREATE ROLE canaima PASSWORD 'c4n41m4' NOSUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;
CREATE DATABASE canaima OWNER canaima;
GRANT ALL PRIVILEGES ON DATABASE canaima to canaima;

Con esto es suficiente, a continuacion lo unico necesario sera ejecutar:

python manage.py makemigrations
python manage.py migrate 

en la carpeta raiz del proyecto para sincronizar la base de datos
