# # mi_archivo = open('Prueba.txt') # r para leer, w para escribir, a para solo escritura al final del archivo, manteniendo el contenido original
# #
# # todas = mi_archivo.readlines() ## a archivos pequeños, ya que jala todoo el archivo y ocupa toda la memoria
# #
# # todas = todas.pop()
# # print(todas)
#
# # for l in mi_archivo:
# #     print(f'Aqui dice: {l}')
# # print(mi_archivo.read()) ## para ver contenido
# # una_linea = mi_archivo.readline() ## lee la primera y luego se salta a la siguiente
# # # print(una_linea)
# # print(una_linea.rstrip().upper()) ## para eliminar el salto de linea
# # una_linea = mi_archivo.readline()
# # print(una_linea)
# # una_linea = mi_archivo.readline()
# # print(una_linea)
# # # una_linea = mi_archivo.readlines()
# # print(una_linea)
#
# # print(mi_archivo.readline()) ## para primera linea
# # print(mi_archivo.readlines(-1)) ## para primera linea
# # mi_archivo.read()
#
# # mi_archivo = open('PruebaRuta.txt','w')
# # mi_archivo.write('Soy el nuevo texto') # para agregar saltos se ocupa \n
# # mi_archivo.write('''Soy el nuevo texto
# # Aqui ando
# # ''')
# #
# # # mi_archivo.writelines(['hola','muindo','aqui','ando'])
# # lista=['hola','muindo','aqui','ando']
# # for p in lista:
# #     mi_archivo.writelines(p+'\n')
# # mi_archivo.writelines('Hola')
# #
# # mi_archivo = open('PruebaRuta.txt','a')
# #
# # mi_archivo.write('Bienvenido')
# #
# #
# #
# #
# # mi_archivo.close() ## siempre cerrar archivo
# #
#
#
# ## PATH,OS directorios para manejo de archivos
#
# import os
# # ruta = os.getcwd()
# # ruta = os.chdir('C:\\Users\\Luis\\python\\ManipulacionArchivos\\Alternativo')
# # ruta = os.makedirs('C:\\Users\\Luis\\python\\ManipulacionArchivos\\Alternativo\\otra')
# # archivo = open('PruebaRuta.txt')
# ruta = 'C:\\Users\\Luis\\python\\ManipulacionArchivos\\Alternativo\\Prueba.txt'
# #
# elemento= os.path.basename(ruta)
# print(elemento)
# # # elemento= os.path.dirname(ruta)
# # elemento= os.path.split(ruta)
# # os.rmdir('C:\\Users\\Luis\\python\\ManipulacionArchivos\\Alternativo\\otra')
# # print(elemento)
# # # print(archivo)
# # archivo  = open(f'{ruta}\\Prueba.txt')
# # print(archivo.read())
#
# # otro_archivo = open('C:\\Users\\Luis\\python\\ManipulacionArchivos\\Alternativo\\PruebaRuta.txt')
# #
# # print(otro_archivo.read()) ##no para los sistemas operativos
#
# from pathlib import Path
#
# carpeta = Path('/Users/Luis/python/ManipulacionArchivos/Alternativo') / 'PruebaRuta.txt'
# # archivo = carpeta / 'PruebaRuta.txt'
#
# mi_archivo =  open(carpeta)
# print(mi_archivo.read())
#

# from pathlib import Path, PureWindowsPath
#
# carpeta = Path('/Users/Luis/python/ManipulacionArchivos/Alternativo/PruebaRuta.txt')
# ruta_windows = PureWindowsPath(carpeta)
# # print(carpeta.read_text())
# # print(carpeta.name)
# # print(carpeta.suffix) #terminacion
# # print(carpeta.stem) #nombre
# # if not carpeta.exists():
# #     print('este archivo no existe')
# # else:
# #     print('Genial si existe')
#
# print(ruta_windows)

from pathlib import Path

base = Path.home() ## una ruta absoluta al ordenador que se eejecute mac/windows
guia = Path(base,"Barcelona","Europa",Path('España',"Sagrada_Familia.txt") )
# guia2 = guia.with_name('La_Pedreda.txt') #cambia el archivo de destino
print(base)
print(guia)
print(guia.parent) ## mover entre rutas como en js con el dom


# print(guia2)