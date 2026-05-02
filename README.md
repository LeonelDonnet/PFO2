# api_tareas
Pfo2 - programacion sobre redes.


# Sistema de Gestión de Tareas con API y Base de Datos

## Descripción

Este proyecto consiste en el desarrollo de una API REST utilizando Flask que permite registrar usuarios, iniciar sesión y mostrar una página de bienvenida. Los datos se almacenan en una base de datos SQLite y las contraseñas se guardan de forma segura mediante hash.

## Tecnologías utilizadas

- Python 3
- Flask
- SQLite
- Werkzeug (para hash de contraseñas)

## Instalación y ejecución

1. Clonar o descargar el proyecto

2. Abrir una terminal en la carpeta del proyecto

3. Crear un entorno virtual (opcional pero recomendado):

# python -m venv venv


4. Activar el entorno virtual:

venv\Scripts\activate

source venv/bin/activate


5. Instalar las dependencias:

pip install flask werkzeug


6. Ejecutar el servidor:

python servidor.py


7. Abrir en el navegador:

http://127.0.0.1:5000/


## Endpoints disponibles

### Registro de usuario

- Método: POST
- URL: /registro
- Body (JSON):

{
"usuario": "nombre",
"contraseña": "1234"
}


Respuesta esperada:

{
"mensaje": "Usuario registrado correctamente"
}



### Inicio de sesión

- Método: POST
- URL: /login
- Body (JSON):

{
"usuario": "nombre",
"contraseña": "1234"
}


Respuesta correcta:

{
"mensaje": "Login exitoso"
}


Respuesta en caso de error:

{
"error": "Credenciales incorrectas"
}



### Página de tareas

- Método: GET
- URL: /tareas

Muestra una página HTML de bienvenida.

## Pruebas

Las pruebas se realizaron utilizando Postman, enviando solicitudes a cada uno de los endpoints y verificando las respuestas.

## Base de datos

El sistema utiliza SQLite, generando automáticamente el archivo `usuarios.db` al iniciar el servidor. En este archivo se almacenan los usuarios registrados.

## Autor

Trabajo práctico realizado como parte de la materia de programación, por Leonel Donnet.


# ¿Por qué hashear contraseñas?

Hashear contraseñas es importante porque permite almacenar las contraseñas de forma segura. En lugar de guardar la contraseña original, se guarda una versión transformada (hash) que no puede convertirse fácilmente en la contraseña real.

Esto protege a los usuarios en caso de que la base de datos sea comprometida, ya que un atacante no podría obtener directamente las contraseñas originales. Además, el uso de funciones de hash seguras evita ataques comunes como el acceso directo a credenciales almacenadas en texto plano.

# Ventajas de usar SQLite en este proyecto

SQLite es una buena opción para este tipo de proyecto porque es una base de datos liviana que no requiere instalación ni configuración adicional. Funciona mediante un solo archivo, lo que facilita su uso y portabilidad.

Además, es suficiente para aplicaciones pequeñas o de prueba, como este trabajo práctico, donde no se necesita manejar grandes volúmenes de datos ni múltiples usuarios concurrentes. También se integra fácilmente con Python, lo que simplifica el desarrollo.