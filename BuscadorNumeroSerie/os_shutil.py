# mas sobre os y shutil
# import os
#
# # print(os.getcwd())
# archivo = open('cursor.txt', 'w')
# archivo.write('Textp de Prueba')
# archivo.close()
#
# print(os.listdir())
#
# import shutil
#
# # # shutil.move('cursor.txt', 'C:\\Users\\Luis\\') ## mover archios os.rm remover carpeta, shutil.mrtree elimana todooo y recursivo
# #
# # import send2trash
# # send2trash.send2trash('C:\\Users\\Luis\\python\\BuscadorNumeroSerie\\cursor.txt')
#
# import os
#
# # print(os.walk('C:\\Users\\Luis\\python'))
#
# ruta = 'C:\\Users\\Luis\\python'
#
# for carpeta, subcarpeta, archivo in os.walk(ruta):
#     print(f'en la carpeta: {carpeta}')
#     print(f'las subcarpetas son: {carpeta}')
#     for sub in subcarpeta:
#         print(f'\t{sub}')
#     print(f'Los archivos son')
#     for arch in archivo:
#         if arch.startswith('p'):
#             print(f'\t{arch}')
#
#     print('\n')

#
# import datetime
#
# mi_hora = datetime.time(17,10,59)
# mi_dia = datetime.date(2000,10,20)
# print(mi_hora.minute)
# print(mi_hora.second)
# print(mi_hora.hour)
#
# print(mi_dia.day)
# print(mi_dia.month)
# print(mi_dia.year)
#
# print(mi_dia.today())
#
# from datetime import datetime
#
# mi_fecha = datetime(2025,5,15,22,10,15,250000)
# mi_fecha = mi_fecha.replace(year=2020)
# print(mi_fecha)
# print(mi_fecha.strftime('%d/%m/%Y %H:%M:%S'))
#
#
# from datetime import date
#
# nacimiento = date(1990,1,1)
# defuncion = date(2025,1,1)
#
# edad = defuncion - nacimiento
# print(edad)
# print(edad.days)
# print(edad.seconds)
# print(edad.total_seconds())

# from datetime import datetime
#
# despierta = datetime(2025,5,15,12,10,15,)
# duerme = datetime(2025,5,15,17,10,14)
# vigilia = duerme-despierta
#
# print(vigilia)
# print(vigilia.seconds)



#math
#
# import math
#
# # resultado = math.floor(8.9)
# # resultado = math.ceil(8.9)
# # resultado = math.pi
# # resultado = math.log(25,5 )
# # resultado = math.tan(256)
# resultado = math.sqrt()
# print(resultado)


 #MODULO RE  -- Expresiones regulares   ---  cuantificadores  {}son para que tome en cuenta cuantos va a contar
 # /d digito numerico
#  /w caracter alfanumerico
# /s espacio en blanco
# /D no es un digito
# /W no Alfanumerico
# /S no espacio en blanco

# ----- CUANTIFICADORES
# +  1 o mas veces \d-\d+
# {n} se repite n veces  \d-\d{4}
# {n,m }
# {n}
## -*
## -* ? 1o mas


# texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas del dia, 7 dias de la semana y 3 semanas de la semana al servicio de ayuda online"
#
# # palabra = 'ayuda' in texto
# # print(palabra)
# import re
#
# patron = 'ayuda'
#
# busqueda = re.findall(patron, texto)
# print(busqueda)
#
# for hallazgo in re.finditer(patron, texto):
#     print(hallazgo.span())
#     print(hallazgo.group())

# buscar por formato
# texto = 'llama al 567-215-6588 ya mismo'
#
# patron = r'\d{3}-\d{3}-\d{4}'
# patron = re.compile( r'(\d{3})-(\d{3})-(\d{4})')
#
# resultado = re.search(patron, texto)
# print(resultado.group(1))

# clave = input("Clave: ")
#
# patron = r'\D{1}\w{7}'
#
# chequear = re.search(patron, clave)
# print(chequear)

# texto = 'No antendemos los jueves por la tarde'


# buscar = re.search(r'...demos...', texto) ## puntos trae lo que tiene a lados
# buscar = re.findall(r'[^\s]+', texto) ## busca por expresion ^ pal inicio , $ pal final, [^] se excluye el patron

# print(''.join(buscar))


# COMPRIMR ARCHIVOS Y DESCOMPRIMIR - zipfile shutil

# import zipfile
#
# mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')
# mi_zip.write('mi_texto_A.txt')
# mi_zip.write('mi_texto_B.txt')
# mi_zip.close()

#
# zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
#
# zip_abierto.extractall()


# import shutil
# import os
# from pathlib import Path
#
# # ruta_general = Path(os.getcwd())
# # ruta = Path(ruta_general.parent, 'ManipulacionArchivos')
# # print(ruta)
# # # print(ruta)
# # # carpeta_origen = 'C:\\Users\\Luis\\python\\BuscadorNumeroSerie'
# # archivo_destino = 'Todo_Comprimido'
# # #
# # shutil.make_archive(archivo_destino, 'zip', ruta)
#
# shutil.unpack_archive('Todo_Comprimido.zip', 'Extraccion terminada','zip')


import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

ruta = 'C:\\Users\\Usuario\\Desktop\\Mi_Gran_Directorio'

mi_patron = r'N\D{3}-\d{5}'

hoy = datetime.date.today()
nros_encontrados = []

archivos_encontrados = []

def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''

def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta,a), mi_patron)
            if resultado != '':
                nros_encontrados.append((resultado.group()))
                archivos_encontrados.append(a.title())

def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de Búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for a in archivos_encontrados:
        print(f'{a}\t{nros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Números encotrados: {len(nros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)

crear_listas()
mostrar_todo()
