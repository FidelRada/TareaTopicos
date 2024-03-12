from flask import Blueprint, jsonify, request
import psycopg2

registros_bp = Blueprint('registros', __name__)

# Configuración de la conexión a PostgreSQL
conn = psycopg2.connect(
    dbname="nombre_de_tu_base_de_datos",
    user="tu_usuario",
    password="tu_contraseña",
    host="localhost"
)

# Crear cursor
cursor = conn.cursor()

# Ruta para obtener todos los registros
@registros_bp.route('/api/registros', methods=['GET'])
def obtener_registros():
    cursor.execute("SELECT * FROM tabla")
    registros = cursor.fetchall()
    return jsonify(registros)

# Ruta para obtener un registro por ID
@registros_bp.route('/api/registros/<int:id>', methods=['GET'])
def obtener_registro_por_id(id):
    cursor.execute("SELECT * FROM tabla WHERE id = %s", (id,))
    registro = cursor.fetchone()
    return jsonify(registro)

# Ruta para crear un nuevo registro
@registros_bp.route('/api/registros', methods=['POST'])
def crear_registro():
    data = request.get_json()
    sql = "INSERT INTO tabla (columna1, columna2) VALUES (%s, %s)"
    val = (data['valor1'], data['valor2'])
    cursor.execute(sql, val)
    conn.commit()
    return jsonify({"message": "Registro creado correctamente"})

# Ruta para actualizar un registro
@registros_bp.route('/api/registros/<int:id>', methods=['PUT'])
def actualizar_registro(id):
    data = request.get_json()
    sql = "UPDATE tabla SET columna1 = %s, columna2 = %s WHERE id = %s"
    val = (data['valor1'], data['valor2'], id)
    cursor.execute(sql, val)
    conn.commit()
    return jsonify({"message": "Registro actualizado correctamente"})

# Ruta para eliminar un registro
@registros_bp.route('/api/registros/<int:id>', methods=['DELETE'])
def eliminar_registro(id):
    sql = "DELETE FROM tabla WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    conn.commit()
    return jsonify({"message": "Registro eliminado correctamente"})
