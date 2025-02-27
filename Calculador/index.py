# tipos de datos
# string(str) 'hola'
# integer(int)  1234
# floating(float) 123.218
# listas(list) ['sal',1,-3,4.5]
# diccionarios(dict) {color:'rojo', arte:'cine'}
# tuples(tuple) ('lun','mar','mie')
# sets(set) {'a','s','d'}
# booleanos(bool) true false

# #variables
# nombre='Juan'
# # print(nombre)
#
# nombre='Laura'
# # print(nombre)

#
# edad = 30
# edad2 = 30
# print(edad + edad2)

# nombre = input('dime tu nombre: ')
# print('tu nombre es: ' + nombre)

# nombre = 'Hola'
# nombre1 = ' Python'
#
# frase = nombre + nombre1
# print(frase)

# mi_numero = 1.55132136518907468787687768077676768786847 + 3
# mi_numero = mi_numero + 5
# print(mi_numero)
# print(type(mi_numero))
#
#
# # Conversion de datos ( Para imprimr tienen que ser del mismo tipo de dato )
# edad = input('Dime tu edad: ')
# print('tu edad es: '+ edad)
#
# nueva_edad = 1+ int(edad)
# print(type(nueva_edad))
# print('Vas a cumplir ' + nueva_edad)
# print('Vas a cumplir ' + str(nueva_edad))

# color_auto = 'rojo'
# matricula = 65486461
# #Format
# print("Mi auto es {} y de matricula {} {}".format(color_auto, matricula,'12'))
#  #Cadenas Literales
# print(f"El color es: {color_auto} y  de matricula {matricula+matricula}")
#
# x=5
# y=10
#
# print("La suma de {} y de {} es {}".format(x,y,x+y))
#
#
# #### Operador Matematicos
# x=6
# y=2
# z=7
# print(f"{x} y {y} suman: {x+y}")
# print(f"{x} y {y} restan: {x-y}")
# print(f"{x} y {y} multiplidos: {x*y}")
# print(f"{x} y {y} divididos: {x/y}")
#
# #Redondeo hacia abajo
# print(f"{z} dividido al piso de {y} es igual {z/y}")
# print(f"{z} dividido al piso de {y} es igual {z//y}")
#
# #Modulo (Restante de la division) para ver si es par tambien podria quedar
# print(f"{z} modulo de {y} es igual {z%y}")
# print(f"{x} elevado a la  {y} divididos: {x**y}")
# print(f"{x} elevado a la  {3} divididos: {x**3}")
# print(f"La raiz cuadrada de {x} es: {x**0.5}")



###### Redondeo
x=6
print(f"La raiz cuadrada de {x} es: {round(x**0.5)}")
m=90/7
print(m)
print(round(m))

valor= 95.666666666666
print(round(valor,2))
