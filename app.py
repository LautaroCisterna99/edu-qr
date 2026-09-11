"""
EDU QR — esqueleto Flask + MySQL (Etapa 1)

Punto de partida para que los equipos 3 (HTML), 4 (CSS), 5 (Python/Flask) y 6
(integración/pruebas) tengan algo funcionando desde el primer día, en lugar de
partir de cero. Ya incluye conexión a MySQL, un buscador con filtros y la
ficha individual de cada escuela.

Cómo se organiza el código (para que cada equipo sepa dónde tocar):
  - Equipo 3 (HTML):        templates/*.html — estructura de las páginas
  - Equipo 4 (CSS):         static/css/style.css — diseño visual y responsive
  - Equipo 5 (Flask/lógica): este archivo (app.py) — rutas y consultas
  - Equipo 6 (integración):  prueba que todo funcione junto, documenta bugs
  - Equipo 2 (base de datos): db/schema.sql y db/seed_data.sql
  - Equipo 1 (relevamiento):  docs/equipo1_relevamiento/ — entrega los datos
                              reales para que el Equipo 2 los cargue

Ver README.md para instrucciones de instalación.
"""

import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

app = Flask(__name__)


def get_conexion():
    """Abre una conexión nueva a MySQL usando los datos del archivo .env."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "edu_qr"),
    )


@app.route("/")
def index():
    """Página principal: lista de escuelas con buscador y filtros."""
    texto_busqueda = request.args.get("q", "").strip()
    orientacion_filtro = request.args.get("orientacion", "").strip()
    turno_filtro = request.args.get("turno", "").strip()

    conexion = get_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
        SELECT DISTINCT e.id, e.nombre, e.tipo_gestion, e.direccion
        FROM escuelas e
        LEFT JOIN escuela_orientacion eo ON eo.escuela_id = e.id
        LEFT JOIN orientaciones o ON o.id = eo.orientacion_id
        LEFT JOIN escuela_turno et ON et.escuela_id = e.id
        LEFT JOIN turnos t ON t.id = et.turno_id
        WHERE 1 = 1
    """
    parametros = []

    if texto_busqueda:
        consulta += " AND e.nombre LIKE %s"
        parametros.append(f"%{texto_busqueda}%")

    if orientacion_filtro:
        consulta += " AND o.nombre = %s"
        parametros.append(orientacion_filtro)

    if turno_filtro:
        consulta += " AND t.nombre = %s"
        parametros.append(turno_filtro)

    consulta += " ORDER BY e.nombre"

    cursor.execute(consulta, parametros)
    escuelas = cursor.fetchall()

    # listas para llenar los <select> de filtros
    cursor.execute("SELECT nombre FROM orientaciones ORDER BY nombre")
    orientaciones = [fila["nombre"] for fila in cursor.fetchall()]

    cursor.execute("SELECT nombre FROM turnos ORDER BY nombre")
    turnos = [fila["nombre"] for fila in cursor.fetchall()]

    cursor.close()
    conexion.close()

    return render_template(
        "index.html",
        escuelas=escuelas,
        orientaciones=orientaciones,
        turnos=turnos,
        texto_busqueda=texto_busqueda,
        orientacion_filtro=orientacion_filtro,
        turno_filtro=turno_filtro,
    )


@app.route("/escuela/<int:escuela_id>")
def ficha_escuela(escuela_id):
    """Ficha individual de una escuela con toda su información."""
    conexion = get_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM escuelas WHERE id = %s", (escuela_id,))
    escuela = cursor.fetchone()

    cursor.execute(
        """
        SELECT o.nombre FROM orientaciones o
        JOIN escuela_orientacion eo ON eo.orientacion_id = o.id
        WHERE eo.escuela_id = %s
        """,
        (escuela_id,),
    )
    orientaciones = [fila["nombre"] for fila in cursor.fetchall()]

    cursor.execute(
        """
        SELECT t.nombre FROM turnos t
        JOIN escuela_turno et ON et.turno_id = t.id
        WHERE et.escuela_id = %s
        """,
        (escuela_id,),
    )
    turnos = [fila["nombre"] for fila in cursor.fetchall()]

    cursor.execute(
        "SELECT pregunta, respuesta FROM preguntas_frecuentes WHERE escuela_id = %s",
        (escuela_id,),
    )
    faqs = cursor.fetchall()

    cursor.execute(
        "SELECT descripcion FROM actividades_extracurriculares WHERE escuela_id = %s",
        (escuela_id,),
    )
    actividades = [fila["descripcion"] for fila in cursor.fetchall()]

    cursor.close()
    conexion.close()

    return render_template(
        "ficha_escuela.html",
        escuela=escuela,
        orientaciones=orientaciones,
        turnos=turnos,
        faqs=faqs,
        actividades=actividades,
    )


if __name__ == "__main__":
    # debug=True solo para desarrollo en clase; sacarlo antes de la Expo.
    app.run(debug=True, host="0.0.0.0", port=5000)
