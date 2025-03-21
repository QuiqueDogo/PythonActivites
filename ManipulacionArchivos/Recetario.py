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
#
# from pathlib import Path
#
# # base = Path.home() ## una ruta absoluta al ordenador que se eejecute mac/windows
# # guia = Path(base,"Barcelona","Europa",Path('España',"Sagrada_Familia.txt") )
# # # guia2 = guia.with_name('La_Pedreda.txt') #cambia el archivo de destino
# # print(base)
# # print(guia)
# # print(guia.parent) ## mover entre rutas como en js con el dom
# #
# #
# # guia = Path(Path.home(),'python','ManipulacionArchivos', 'Europa')
# # # **/*.txt busca todas las capertas q contengan txt
# # for text in Path(guia).glob('**/*.txt'): ## itera como un arbol de la ubicacion actual
# #     print(text)
# # print(guia)
#
# guia = Path('Europa', 'España',"Barcelona", "Sagrada_Familia.txt")
# en_europa = guia.relative_to(Path("Europa"))
# en_espania = guia.relative_to(Path("Europa","España"))
# print(guia)
# print(en_europa)
# print(en_espania)
#
#
# from os import system
#
# ## LIMPIAR CONSOLA
# nombre = input('Dime nombre:')
# edad = input('Dime edad:')
#
# system('cls')
# print(f'Tu nombre es {nombre} y tienes {edad} años')
# ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
# print(ruta)
# print(ruta.parents[0])


from os import system
from pathlib import Path

ruta_home = Path('Recetas').resolve()

def comprobar_opcion(opcion):
    elegida = int(opcion)
    try:
        elegida = int(opcion)
    except ValueError:
        print('Tiene que ser un numero de la lista. Intenta de nuevo')
        elegida = input('Selecciona un numero: ')
        elegida = int(elegida)
    if elegida > 6 or 1 > elegida:
        print('Tiene que ser un numero de la lista. Intenta de nuevo')
        elegida = input('Selecciona un numero: ')
        elegida = int(elegida)

    return elegida

def bienvenida_recetario():
    print(f'Bienvenido al Recetario. La ruta para las recetas se encuentra en: {ruta_home}.\nPor favor elige una'
      f'de las siguientes opciones:\n'
      f'[1] - Leer Receta\n'
      f'[2] - Crear Receta\n'
      f'[3] - Crear Categoria\n'
      f'[4] - Eliminar Receta\n'
      f'[5] - Eliminar Categoria\n'
      f'[6] - Finalizar Programa'
      )

def pedir_opcion():
    data = input('Selecciona un numero: ')
    return data

bienvenida_recetario()
opcion_elegida = pedir_opcion()
opcion_elegida = comprobar_opcion(opcion_elegida)

sigue = True

# def reset_menu():
#     bienvenida_recetario()
#     opcion_elegida = pedir_opcion()
#     opcion_elegida = comprobar_opcion(opcion_elegida)

def leer_receta():
    print('Estos son los pri')
    print(ruta_home)
    x = [{index: child} for index, child in enumerate(ruta_home.iterdir()) if child.is_dir()]
    for child in ruta_home.iterdir():
        if child.is_dir():
            print(child)
    print(x[0].items())


def salir_progrma():
    sigue = False
    print('Hasta luego')

def default_case():
    return 'Invalid case'

def switch_case(value):
    switch = {
        1: leer_receta,
        6: salir_progrma,
    }
    return switch.get(value, default_case)()




while sigue:
    sigue = switch_case(opcion_elegida)
    # print(result)


    # system('cls')
    print(opcion_elegida, type(opcion_elegida))





