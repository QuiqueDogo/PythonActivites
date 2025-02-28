# mi_texto = 'Esta es una prueba'
# # resultado = mi_texto[9]
# # resultado = mi_texto.index('a', 5, 11) #para buscar /inicio indice
# resultado = mi_texto.rindex('a') #al reves
# print(resultado)
# print(resultado)

### Extraer substring slicing
# texto = 'ABCDEFGHIJKLM'
# # fragmento = texto[2:] #donde de indica hasta n
#
# # fragmento = texto[:5] #desde el principio hasta donde n
# # fragmento = texto[::-1] # texto al revez
# fragmento = texto[2:10:2] # tomara del 2 al 10 saltando 2 caracteres es el ultimo indice para saltear
# print(fragmento)

#upper() pasar a mayusculas
#lower() pasar a minisculas
#split() separarlo en partes (listas)
# join() - unir items usando separador
# find() , replace()

# texto = "Este es un texto Mio de luis"
# resultado = texto.upper()
# resultado = texto[2].upper()
# resultado = texto.lower()
# resultado = texto.split()
# # resultado = texto.split('t') #criterio de separacion
# a='Aprender'
# b="Python"
# c='es'
# d='genial'
# e = "-".join([a,b,c,d])
# # resultado = texto.

# # resultado=texto.find('textosa')  #-1 es por que no encuentra
# resultado=texto.replace('e' , 'x')
#
# print(resultado)

####### PROPIEDAD DE STRING
# inmutables , concatenables, multilineales ''' '''
# verificar si contiene
# texto= 'hola mundo'
# print('hola' in texto) # TRUE
# largo length

# nombre='carina'
# nombre[0] = 'k'
# print(nombre) #aqui no se puede reasginar

# multiplar string
# n1='Kari'
# n2='na'
# print(n1*10)

# poema = '''mil pequeños peces blancos
#     como si hirviera
# el color del agua'''
# print(poema)
# print(' ' in  poema)
# print('sol' in  poema)
# print('agua' not in  poema)
# poema = 'hola mundo'
# print(len(poema))


##### Listas
# Se pueden mutar
# Puede tener varios tipos de datos, se separan por commas y  se anidar mas listas

# mis_listas=['a','b','c']
# # otras=['a',55,True]
# # resultado = len(mis_listas)
# # resultado= mis_listas[0]
# mi_lista2 = ['d','f' ,'e']
# mi_lista3 = mis_listas + mi_lista2
# # resultado= mis_listas[:+ mi_lista2
# # resultado= mis_listas[:1]
# # mis_listas[0] = 'prueba'
# # mi_lista3.append('g') ## agregar nuevo indice o elementos
# eliminado = mi_lista3.pop(1)
#
# print(mi_lista3)
# print(eliminado)

# ORDENAMIENTO
lista = ['g','a','e','b']
lista.sort()
lista.reverse()
# no se puede almacetar de momento asi no listanueva = lista.sort(),  mientras no la asigne a otra si se puede
lista_nueva = lista
print(lista)