import os
import shutil

def organizar_archivos_por_tipo(directorio):
    # Definir las carpetas de destino para cada tipo de archivo
    carpetas_destino = {
        '.png': 'imagenes',
        '.jpg': 'imagenes',
        '.jpeg': 'imagenes',
        '.gif': 'imagenes',
        '.bmp': 'imagenes',
        '.zip': 'comprimidos',
        '.rar': 'comprimidos',
        '.tar': 'comprimidos',
        '.gz': 'comprimidos',
        '.7z': 'comprimidos',
        '.pdf': 'documentos',
        '.doc': 'documentos',
        '.docx': 'documentos',
        '.csv': 'documentos',
        '.xls': 'documentos',
        '.py': 'comprimidos',
        '.xlsx': 'documentos',
        '.ppt': 'documentos',
        '.pptx': 'documentos',
        '.one': 'documentos',
        '.txt': 'documentos',
        '.mp3': 'audio',
        '.wav': 'audio',
        '.ogg': 'audio',
        '.mp4': 'video',
        '.avi': 'video',
        '.mkv': 'video',
        '.mov': 'video',
        '.psc': 'Tareas Anahi',

    }

    # Crear las carpetas de destino si no existen
    for carpeta in set(carpetas_destino.values()):
        ruta_carpeta = os.path.join(directorio, carpeta)
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)

    # Mover los archivos a sus carpetas correspondientes
    for archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, archivo)
        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1].lower()
            if extension in carpetas_destino:
                carpeta_destino = os.path.join(directorio, carpetas_destino[extension])
                shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))

# Ruta del directorio a organizar
directorio = 'C:/Users/wilme/Desktop'

# Llamar a la función para organizar los archivos
organizar_archivos_por_tipo(directorio)
