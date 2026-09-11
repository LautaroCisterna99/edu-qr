-- EDU QR — Datos de prueba
--
-- Escuelas FICTICIAS para que los equipos 3, 4, 5 y 6 puedan trabajar sin
-- depender de que el relevamiento (Equipo 1) ya haya terminado. Cuando las
-- escuelas reales estén confirmadas y autorizadas, el Equipo 2 reemplaza
-- estos datos por los reales (ver docs/equipo1_relevamiento/).

USE edu_qr;

INSERT INTO orientaciones (nombre) VALUES
    ('Técnica en Informática'),
    ('Técnica en Electromecánica'),
    ('Técnica en Construcciones'),
    ('Técnica en Química');

INSERT INTO turnos (nombre) VALUES
    ('Mañana'), ('Tarde'), ('Noche');

INSERT INTO escuelas
    (nombre, tipo_gestion, direccion, telefono, email,
     requisitos_inscripcion, documentacion_necesaria,
     fecha_inicio_inscripcion, fecha_fin_inscripcion)
VALUES
    ('EICO - Escuela Industrial de Caleta Olivia (dato de prueba)', 'publica',
     'Av. Ejemplo 123, Caleta Olivia', '297-4000000', 'contacto@ejemplo.edu.ar',
     'Certificado de 7.° grado aprobado', 'DNI, partida de nacimiento, certificado de vacunación',
     '2026-10-01', '2026-11-30'),

    ('Escuela Técnica N.° 2 (dato de prueba)', 'publica',
     'Calle Ficticia 456, Caleta Olivia', '297-4000001', 'contacto2@ejemplo.edu.ar',
     'Certificado de 7.° grado aprobado', 'DNI, partida de nacimiento',
     '2026-10-01', '2026-11-15'),

    ('Instituto Técnico Privado Ejemplo (dato de prueba)', 'privada',
     'Ruta 3 Km 5, Caleta Olivia', '297-4000002', 'info@institutoejemplo.edu.ar',
     'Certificado de 7.° grado aprobado, entrevista familiar', 'DNI, partida de nacimiento, ficha médica',
     '2026-09-15', '2026-10-31');

INSERT INTO escuela_orientacion (escuela_id, orientacion_id) VALUES
    (1, 1), (1, 2),
    (2, 3),
    (3, 1), (3, 4);

INSERT INTO escuela_turno (escuela_id, turno_id) VALUES
    (1, 1), (1, 2),
    (2, 1),
    (3, 2), (3, 3);

INSERT INTO preguntas_frecuentes (escuela_id, pregunta, respuesta) VALUES
    (1, '¿Hay que rendir examen de ingreso?', 'No, el ingreso es directo con la documentación completa (dato de prueba).'),
    (1, '¿Tiene comedor escolar?', 'Sí, de lunes a viernes en horario de turno completo (dato de prueba).');
