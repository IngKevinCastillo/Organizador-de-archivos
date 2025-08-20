import os
import shutil

extensions_dict = {
    '.txt': 'documentos',
    '.doc': 'documentos',
    '.docx': 'documentos',
    '.xls': 'documentos',
    '.xlsx': 'documentos',
    '.ppt': 'documentos',
    '.pptx': 'documentos',
    '.pdf': 'documentos',

    '.jpg': 'imagenes',
    '.jpeg': 'imagenes',
    '.png': 'imagenes',
    '.gif': 'imagenes',
    '.bmp': 'imagenes',
    '.ico': 'imagenes',
    '.svg': 'imagenes',

    '.mp4': 'videos',
    '.mkv': 'videos',
    '.avi': 'videos',
    '.mov': 'videos',
    '.wmv': 'videos',
    '.flv': 'videos',

    '.py': 'programacion',
    '.java': 'programacion',
    '.c': 'programacion',
    '.cpp': 'programacion',
    '.cs': 'programacion',
    '.js': 'programacion',
    '.ts': 'programacion',
    '.html': 'programacion',
    '.css': 'programacion',
    '.php': 'programacion',

    '.mcpack': 'minecraft',
    '.mcaddon': 'minecraft',
    '.mcworld': 'minecraft',

    '.apk': 'apk',

    '.exe': 'ejecutable',
    '.msi': 'ejecutable'
}

predeterminada = 'otros'
carpeta_organizar_ruta = r'ruta completa de la carpeta'

archivos = os.listdir(carpeta_organizar_ruta)

for archivo in archivos:
    archivo_origen_ruta = os.path.join(carpeta_organizar_ruta, archivo)

    if os.path.isfile(archivo_origen_ruta):
        _, extension = os.path.splitext(archivo)
        extension = extension.lower()

        carpeta_destino = extensions_dict.get(extension, predeterminada)
        carpeta_destino_ruta = os.path.join(carpeta_organizar_ruta, carpeta_destino)

        if not os.path.exists(carpeta_destino_ruta):
            os.makedirs(carpeta_destino_ruta)

        shutil.move(archivo_origen_ruta, os.path.join(carpeta_destino_ruta, archivo))

print("Archivos organizados correctamente.")
