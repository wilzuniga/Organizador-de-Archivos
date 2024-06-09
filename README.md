
# Organizador de Archivos por Tipo

Este script de Python organiza los archivos de un directorio específico en subcarpetas según su tipo (por ejemplo, imágenes, archivos comprimidos, documentos, etc.).

## Características

- Organiza archivos en subcarpetas basadas en sus extensiones.
- Soporta múltiples tipos de archivos (imágenes, comprimidos, documentos, audio, video).
- Crea automáticamente las subcarpetas necesarias si no existen.

## Requisitos

- Python 3.x

## Instalación

1. Clona este repositorio en tu máquina local:



    `[    git clone https://github.com/tuusuario/organizador-archivos.git
    ](https://github.com/wilzuniga/Organizador-de-Archivos.git)`

2. Navega al directorio del proyecto:

    `
    cd organizador-archivos
    `

## Uso

1. Abre el archivo `organizador.py` y edita la variable `directorio` con la ruta del directorio que deseas organizar.

    `
    directorio = '/ruta/a/tu/carpeta'
    `

2. Ejecuta el script:

    `
    python organizador.py
    `


## Extensiones Soportadas

Por defecto, el script soporta las siguientes extensiones y las organiza en las carpetas correspondientes:

- **Imágenes**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`
- **Comprimidos**: `.zip`, `.rar`, `.tar`, `.gz`, `.7z`
- **Documentos**: `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.txt`
- **Audio**: `.mp3`, `.wav`, `.ogg`
- **Video**: `.mp4`, `.avi`, `.mkv`, `.mov`

Puedes modificar estas configuraciones editando el diccionario `carpetas_destino` en `organizador.py`.
