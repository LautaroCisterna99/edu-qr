# EDU QR — Esqueleto técnico (Etapa 1)

Guía digital de escuelas secundarias técnicas de Caleta Olivia, desarrollada por y para estudiantes de 4.º año. Este repositorio es el punto de partida para que los equipos de programación (2, 3, 4, 5 y 6) extiendan el proyecto en lugar de comenzar de cero. El Equipo 1 no necesita este código para relevar escuelas: usa `docs/equipo1_relevamiento/planilla_relevamiento.md`.

## Qué hace ya (v0.3 de la metodología incremental)

- Buscador de escuelas por nombre.
- Filtro por orientación y por turno.
- Ficha individual de cada escuela con mapa embebido, contacto, inscripción y (si existen) actividades y preguntas frecuentes.
- Base de datos MySQL relacional con datos de prueba, para no depender de que el relevamiento ya haya terminado.
- Generador de código QR apuntando a la plataforma.

## Qué carpeta le corresponde a cada equipo

| Equipo | Carpeta / archivo |
| --- | --- |
| 1 — Relevamiento | `docs/equipo1_relevamiento/` |
| 2 — Base de datos | `db/schema.sql`, `db/seed_data.sql` |
| 3 — HTML | `templates/` |
| 4 — CSS y diseño | `static/css/style.css` |
| 5 — Python / Flask | `app.py`, `qr/generar_qr.py` |
| 6 — Integración y pruebas | `docs/equipo6_integracion/checklist_pruebas.md` |

Todos los equipos comparten el mismo repositorio: no hay un repo por equipo. La idea es que cada uno trabaje principalmente en su carpeta, pero cualquiera puede leer el resto para entender cómo funciona el sistema completo (eso también lo va a pedir la evaluación individual).

## Instalación (una vez por equipo/máquina)

Guía pensada para Windows (lo que usa la mayoría en el aula), con las equivalencias de Mac/Linux entre paréntesis. Va con más detalle del habitual porque son los pasos donde más problemas suelen aparecer la primera vez — seguirlos en orden ahorra tiempo.

### 0. Antes de empezar

- Conexión a internet (solo para descargar los instaladores, una vez).
- Contar con permisos de administrador en la compu para instalar programas.
- La primera vez lleva 30-40 minutos; las siguientes instalaciones son mucho más rápidas.

### 1. Instalar Python

Descargar de [python.org/downloads](https://www.python.org/downloads/) — preferir una versión **3.11 o 3.12** en lugar de la más nueva disponible (ver nota abajo). Durante la instalación, en la primera pantalla, **tildar "Add python.exe to PATH"** — si no se tilda, la terminal después no va a reconocer el comando `python`.

Verificar abriendo una terminal nueva y corriendo:

```
python --version

```

> **Por qué no la versión más nueva de Python:** algunas librerías (como Pillow, que usa el generador de QR) tardan un tiempo en publicar instaladores listos para cada versión nueva de Python. Si usás una versión recién salida (por ejemplo 3.13 o 3.14), `pip install` puede intentar compilar la librería desde cero y fallar con un error que menciona "Microsoft Visual C++", "zlib" o "Failed building wheel for Pillow". El `requirements.txt` de este proyecto ya está armado sin versiones fijas para minimizar esto, pero si el error aparece igual, la solución más simple es instalar Python 3.11 o 3.12 en paralelo y usar esa versión para este proyecto (se puede tener más de una versión de Python instalada a la vez).

### 2. Instalar la base de datos: XAMPP (recomendado) o MySQL Server

**Opción recomendada — XAMPP:** incluye MySQL (compatible, es MariaDB por dentro) y **phpMyAdmin**, una interfaz web que permite cargar los datos sin usar la terminal — la más fácil para alguien que recién arranca.

1. Descargar de [apachefriends.org](https://www.apachefriends.org/) e instalar con las opciones por defecto.
2. Abrir el **Panel de Control de XAMPP** y click en **"Start"** al lado de **MySQL** (no hace falta iniciar Apache para este proyecto).
3. Importante: el usuario `root` de XAMPP **no tiene contraseña por defecto**. Dejar `DB_PASSWORD` vacío en el `.env` (paso 6).

**Opción alternativa — MySQL Community Server:** si preferís instalarlo por separado, bajalo de [dev.mysql.com/downloads/installer](https://dev.mysql.com/downloads/installer/), elegí el tipo de instalación **"Developer Default"** (incluye MySQL Workbench, una GUI también útil), y durante la instalación configurá una contraseña para `root` — anotala, va en el `.env`. A diferencia de XAMPP, acá el servidor se instala como servicio de Windows: si más adelante `mysql` no conecta con "Can't connect to MySQL server", revisar en `services.msc` que el servicio (`MySQL80` o similar) esté "En ejecución".

> Con cualquiera de las dos opciones: si la terminal dice que no reconoce el comando `mysql`, es porque su carpeta `bin` no quedó en el PATH de Windows. Se puede usar la ruta completa al ejecutable (`C:\xampp\mysql\bin\mysql.exe` para XAMPP, o `C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe` para MySQL Server — el número de versión puede variar) en lugar de escribir solo `mysql`, o agregar esa carpeta al PATH desde "Variables de entorno del sistema" y volver a abrir la terminal.

### 3. Descomprimir el proyecto

Descomprimir `edu-qr-app.zip` donde prefieras, y abrir una terminal parada adentro de esa carpeta:

```
cd ruta\a\edu-qr-app
```

### 4. Crear y activar el entorno virtual

```
python -m venv venv
```

Activarlo (el comando cambia según la terminal):

- **PowerShell:** `venv\Scripts\Activate.ps1` — si tira un error de permisos ("execution of scripts is disabled"), lo más simple es usar el **Símbolo del sistema (cmd)** en lugar de PowerShell para este proyecto.
- **Símbolo del sistema (cmd):** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

El prompt de la terminal debería empezar con `(venv)`. Si no aparece, no seguir: `pip install` instalaría las librerías en el Python global de la compu en lugar del entorno del proyecto.

### 5. Instalar las dependencias

```
pip install -r requirements.txt
```

Si aparece un error de compilación mencionando Pillow (`zlib`, `Failed building wheel`), volver a la nota del paso 1 sobre la versión de Python.

### 6. Configurar la conexión a la base de datos

```
copy .env.example .env
```

(en Mac/Linux: `cp .env.example .env`)

Abrir el archivo `.env` con el Bloc de notas:

- Si instalaste **XAMPP**: dejar `DB_PASSWORD=` vacío.
- Si instalaste **MySQL Server standalone**: completar `DB_PASSWORD` con la contraseña de `root` que configuraste en el paso 2.

### 7. Crear la base y cargar los datos de prueba

**Opción recomendada (sin terminal) — phpMyAdmin, si usás XAMPP:**

1. Con MySQL corriendo en el Panel de XAMPP, abrir `http://localhost/phpmyadmin` en el navegador.
2. Pestaña **"Importar"** → "Seleccionar archivo" → elegir `db\schema.sql` → botón **"Continuar"**.
3. Repetir el mismo paso con `db\seed_data.sql`.

**Opción por terminal:**

En PowerShell, el operador `<` no funciona (da error "está reservado para uso futuro") — usar `Get-Content` en su lugar:

```
Get-Content db\schema.sql | mysql -u root -p
Get-Content db\seed_data.sql | mysql -u root -p
```

Si usás XAMPP (contraseña vacía), sacar el `-p`. Si `mysql` no se reconoce como comando, anteponer la ruta completa entre comillas con `&`, por ejemplo:

```
Get-Content db\schema.sql | & "C:\xampp\mysql\bin\mysql.exe" -u root
```

En el Símbolo del sistema (cmd), el `<` sí funciona normalmente:

```
mysql -u root -p < db\schema.sql
mysql -u root -p < db\seed_data.sql
```

### 8. Correr el sitio

```
python app.py
```

Abrir `http://localhost:5000` en el navegador. Deberían aparecer las 3 escuelas de prueba (podés probar el buscador, los filtros y entrar a una ficha).

### 9. (Opcional) Generar el código QR

```
python qr/generar_qr.py
```

El día de la Expo, generarlo apuntando a la IP real de la compu que va a estar corriendo el sitio en el salón (se consigue con `ipconfig`, buscando "Dirección IPv4"; el celular debe estar en la misma red Wi-Fi):

```
python qr/generar_qr.py http://192.168.0.15:5000
```

## Cuando el Equipo 2 tenga datos reales del Equipo 1

Reemplazar (o complementar) el contenido de `db/seed_data.sql` con las escuelas reales relevadas y autorizadas, manteniendo la misma estructura de tablas de `db/schema.sql`. No hace falta tocar `app.py` ni los templates: las consultas ya están escritas para cualquier cantidad de escuelas.

## Flujo de trabajo con Git / GitHub

Siguiendo la metodología del proyecto (repositorio común, integración semanal):

1. Un solo repositorio en GitHub para los 6 equipos (crearlo como organización o repo compartido con todos como colaboradores).
2. Cada equipo trabaja en su propia rama: `equipo2-basededatos`, `equipo3-html`, `equipo4-css`, `equipo5-flask`, `equipo6-pruebas`.
3. En la reunión semanal de integración, cada equipo hace un Pull Request de su rama a `main` (o pide ayuda al docente/Equipo 6 para mergear).
4. Antes de cada integración, tirar de `main` (`git pull origin main`) para evitar conflictos grandes.
5. `main` siempre debe quedar en un estado funcional — es la versión que se muestra si algo falla en la Expo (ver metodología de versiones incrementales en el documento maestro).

## Errores comunes

| Error / síntoma | Causa más probable | Solución |
| --- | --- | --- |
| `Failed building wheel for Pillow` / menciona `zlib` o `Microsoft Visual C++` al correr `pip install -r requirements.txt` | Versión de Python muy nueva (3.13/3.14) sin instalador precompilado para esa librería | Confirmar que `requirements.txt` no tenga versiones fijas (`==`); si el error persiste, instalar Python 3.11 o 3.12 en paralelo y usar esa versión |
| `pip` o `python` "no se reconoce como un comando" | Python no quedó agregado al PATH al instalarlo | Reinstalar Python tildando "Add python.exe to PATH", o agregarlo manualmente desde "Variables de entorno del sistema" |
| `El operador '<' está reservado para uso futuro` (PowerShell) | PowerShell no soporta la redirección `<` de cmd/bash | Usar `Get-Content archivo.sql \| mysql ...` en su lugar, o cambiar a la terminal "Símbolo del sistema" (cmd) |
| `"mysql" no se reconoce como un comando interno o externo` | La carpeta `bin` de MySQL/XAMPP no está en el PATH | Usar la ruta completa al ejecutable (`C:\xampp\mysql\bin\mysql.exe` o similar) o agregarla al PATH y reabrir la terminal |
| `ERROR 2002: Can't connect to MySQL server on 'localhost'` | El servicio de MySQL no está corriendo | Si usás XAMPP: iniciar MySQL desde el Panel de Control. Si usás MySQL Server: revisar el servicio en `services.msc` |
| `ERROR 1045: Access denied for user 'root'@'localhost'` | Contraseña incorrecta (con XAMPP, lo más común es asumir que hay contraseña cuando en realidad está vacía) | Con XAMPP, conectar sin `-p` (contraseña vacía); con MySQL Server, usar la contraseña definida al instalarlo |
| `Access denied for user` al correr `python app.py` (no al cargar el SQL) | `DB_PASSWORD` en `.env` no coincide con la real | Revisar `.env`: vacío para XAMPP, la contraseña de `root` para MySQL Server |
| `Unknown database 'edu_qr'` | Falta correr `db/schema.sql` (o falló silenciosamente) | Repetir el paso 7, revisando que no haya tirado ningún error en el camino |
| La página carga pero no aparecen escuelas | Falta correr `db/seed_data.sql`, o los filtros no coinciden con ningún dato cargado | Repetir el paso 7, o borrar los filtros de búsqueda en la página |
| El QR no abre el sitio desde el celular | El celular no está en la misma red que la compu, o se generó el QR con `localhost` en vez de la IP real | Usar `ipconfig` para conseguir la IP de la compu, y generar el QR con `python qr/generar_qr.py http://ESA_IP:5000` estando ambos en el mismo Wi-Fi |
