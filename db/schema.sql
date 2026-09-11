-- EDU QR — Modelo relacional (Equipo 2: Base de datos)
--
-- Diseño normalizado: una escuela puede tener varias orientaciones y varios
-- turnos, así que se resuelven como tablas intermedias (muchos a muchos) en
-- lugar de columnas repetidas. La info "extendida" (galería, FAQ, actividades)
-- vive en tablas propias porque una escuela puede tener 0, 1 o varias.

CREATE DATABASE IF NOT EXISTS edu_qr CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE edu_qr;

-- ---------------------------------------------------------------------
-- Tabla principal
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS escuelas (
    id                          INT AUTO_INCREMENT PRIMARY KEY,
    nombre                      VARCHAR(150) NOT NULL,
    tipo_gestion                ENUM('publica', 'privada') NOT NULL,
    direccion                   VARCHAR(250) NOT NULL,
    telefono                    VARCHAR(50),
    email                       VARCHAR(120),
    requisitos_inscripcion      TEXT,
    documentacion_necesaria     TEXT,
    fecha_inicio_inscripcion    DATE,
    fecha_fin_inscripcion       DATE,
    -- campos extendidos simples (no bloquean la carga si faltan)
    fotografia_url              VARCHAR(255),
    video_url                   VARCHAR(255),
    redes_sociales              VARCHAR(255),
    creado_en                   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------
-- Orientaciones (muchos a muchos con escuelas)
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS orientaciones (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    nombre  VARCHAR(80) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS escuela_orientacion (
    escuela_id      INT NOT NULL,
    orientacion_id  INT NOT NULL,
    PRIMARY KEY (escuela_id, orientacion_id),
    FOREIGN KEY (escuela_id) REFERENCES escuelas(id) ON DELETE CASCADE,
    FOREIGN KEY (orientacion_id) REFERENCES orientaciones(id) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------
-- Turnos (muchos a muchos con escuelas)
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS turnos (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    nombre  VARCHAR(30) NOT NULL UNIQUE   -- Mañana / Tarde / Noche
);

CREATE TABLE IF NOT EXISTS escuela_turno (
    escuela_id  INT NOT NULL,
    turno_id    INT NOT NULL,
    PRIMARY KEY (escuela_id, turno_id),
    FOREIGN KEY (escuela_id) REFERENCES escuelas(id) ON DELETE CASCADE,
    FOREIGN KEY (turno_id) REFERENCES turnos(id) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------
-- Información extendida (uno a muchos) — no bloquea la entrega si está vacía
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS actividades_extracurriculares (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    escuela_id  INT NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    FOREIGN KEY (escuela_id) REFERENCES escuelas(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS galeria_imagenes (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    escuela_id  INT NOT NULL,
    url         VARCHAR(255) NOT NULL,
    descripcion VARCHAR(150),
    FOREIGN KEY (escuela_id) REFERENCES escuelas(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS preguntas_frecuentes (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    escuela_id  INT NOT NULL,
    pregunta    VARCHAR(255) NOT NULL,
    respuesta   TEXT NOT NULL,
    FOREIGN KEY (escuela_id) REFERENCES escuelas(id) ON DELETE CASCADE
);
