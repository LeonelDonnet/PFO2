from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def crear_db():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            contraseña TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

crear_db()


@app.route('/')
def inicio():
    return "Servidor funcionando"


@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    
    usuario = data.get('usuario')
    contraseña_plana = data.get('contraseña')
    contraseña = generate_password_hash(contraseña_plana)

    if not usuario or not contraseña:
        return jsonify({"error": "Faltan datos"}), 400

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)", 
                   (usuario, contraseña))

    conn.commit()
    conn.close()

    return jsonify({"mensaje": "Usuario registrado correctamente"})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute("SELECT contraseña FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()

    conn.close()

    if resultado and check_password_hash(resultado[0], contraseña):
        return jsonify({"mensaje": "Login exitoso"})
    else:
        return jsonify({"error": "Credenciales incorrectas"}), 401
    

@app.route('/tareas', methods=['GET'])
def tareas():
    return """
    <html>
        <head>
            <title>Sistema de Tareas</title>
        </head>
        <body>
            <h1>Bienvenido al sistema de gestión de tareas</h1>
            <p>API funcionando correctamente</p>
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True)
