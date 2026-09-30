"""
EDU QR — esqueleto Flask + MySQL (Etapa 1)

Punto de partida para que los equipos 3 (HTML), 4 (CSS), 5 (Python/Flask) y 6
(integración/pruebas) tengan algo funcionando desde el primer día, en lugar de
partir de cero. Trae la conexión a MySQL ya resuelta — lo que falta armar es
la lógica de cada vista (Equipo 5) y lo que se ve en pantalla (Equipos 3 y 4).

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
    """Página principal: lista de escuelas con buscador y filtros.

    TODO (Equipo 5):
    - Leer los parámetros de búsqueda con request.args.get(...): "q" (texto),
      "orientacion" y "turno".
    - Conectarse a la base con get_conexion() y armar la consulta SQL,
      aplicando esos filtros solo si vienen completados.
    - Renderizar templates/index.html pasándole (nombres que el template
      ya espera): escuelas, orientaciones, turnos, texto_busqueda,
      orientacion_filtro, turno_filtro.
    """
    pass  # sacar este pass cuando agreguen el código de arriba


@app.route("/escuela/<int:escuela_id>")
def ficha_escuela(escuela_id):
    """Ficha individual de una escuela con toda su información.

    TODO (Equipo 5):
    - Traer de la base la escuela con ese id (y sus orientaciones, turnos,
      actividades y preguntas frecuentes si corresponde).
    - Renderizar templates/ficha_escuela.html con esos datos.
    """
    pass  # sacar este pass cuando agreguen el código de arriba


if __name__ == "__main__":
    # debug=True solo para desarrollo en clase; sacarlo antes de la Expo.
    app.run(debug=True, host="0.0.0.0", port=5000)
