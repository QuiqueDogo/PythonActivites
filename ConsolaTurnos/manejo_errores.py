"""
Este es un modulo que imprime algo
"""

# try except finally

# def suma():
#     n1 =  int(input('numero 1:'))
#     n2 =  int(input('numero 2:'))
#     print(n1+n2)
#     print('Gracias por sumar' + n1)
#     # print(10+10)
#
# # suma()
#
# try:
#     #codigo a probar
#     suma()
# except TypeError:
#     #codigo a ejecutar tras error
#     print('Estas intentando concatenar tipos distintos')
#     # print('Algo no ha salido bien')
# except ValueError:
#     print('Ese no es un numero')
# else:
#     print('Hiciste todos bien')
#     #coodigo a ejecutar si no hay un error
# finally:
#     print('Eso fue todos!')
#     #codigo a ejecutar al final de todos modos

# ## funcion para asegurar el tipo de valor
# def pedir_numero():
#     while True:
#         try:
#             numero = int(input('dame tu numero'))
#         except:
#             print('Ese es no un numero')
#         else:
#             print(f'Ingresaste el numero {numero}')
#             break
#
#     print('Gracias')
#
# pedir_numero()

# pylint y unitest - buscar errores con pylint
# pylint nombre_archivo.py -r y (saca una tabla con informacion de reporte)
def una_funcion():
    numero1 = 500
    print(numero1)

una_funcion()