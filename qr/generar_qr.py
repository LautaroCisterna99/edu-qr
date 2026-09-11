"""
EDU QR — generador de códigos QR (Etapa 5, adelantado para pruebas tempranas)

Genera un código QR que apunta a la URL de la plataforma y lo guarda en
static/qr/. Para la Expo, cambiar BASE_URL por la dirección donde esté
corriendo el sitio ese día (puede ser una IP local de la red del salón).

Uso:
    python qr/generar_qr.py
    python qr/generar_qr.py http://192.168.0.15:5000
"""

import sys
from pathlib import Path

import qrcode

BASE_URL_POR_DEFECTO = "http://localhost:5000"


def generar_qr(url: str, nombre_archivo: str = "static/qr/edu_qr.png") -> None:
    imagen = qrcode.make(url)
    Path(nombre_archivo).parent.mkdir(parents=True, exist_ok=True)
    imagen.save(nombre_archivo)
    print(f"QR generado para '{url}' -> {nombre_archivo}")


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else BASE_URL_POR_DEFECTO
    generar_qr(url)
