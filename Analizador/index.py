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
# lista = ['g','a','e','b']
# lista.sort()
# lista.reverse()
# # no se puede almacetar de momento asi no listanueva = lista.sort(),  mientras no la asigne a otra si se puede
# lista_nueva = lista
# print(lista)


# ### DICCIONARIO (dict)( en formato seria como un objeto en js pero aqui no se ordenan )  c = {'nombre':'valor1'},
# Valores se pueden repetir pero la claves no
# # c['nombre'] >>>  'valor1'
# diccionario = { 'c1': 'valor1', 'c2':'valor2'}
# # print(type(diccionario))
# print(diccionario)
#
# resultado = diccionario['c1']
# print(resultado)
#
# cliente = {'nombre': 'Juan', 'apellido':'Fuentes', 'peso': 88, 'talla': 1.76}
# consulta = cliente['talla']
# print(consulta)
#
# dic = { 'c1':55,'c2':[10,20,30], 'c3': {'s1':100, 's2':200}}
# # print(dic['c2'][0])
# print(dic['c3']['s1'])
#
# dic2 = {'c1':['a','b','c'], 'c2':['d','e','f']}
# resultado2 = (dic2['c2'][1]).upper()
# print(resultado2)
#
# # anidar elementos a diccionarios y sobreescribir
# dic3 = {1:'a',2:'b'}
# print(dic3)
# dic3[3] = 'c'
# dic3['4'] = 'c'
# print(dic3)
# dic3[2] = 'B'
# print(dic3)
#
# print(dic3.keys()) #key
# print(dic3.values()) #valores
# print(dic3.items()) #tuples


##### TUPLES (son iguales que las listas pero estas son inmutables y van con corchetes) suelen ocupas menos espacio de memoria,
# mi_tuple = (1,2,3,4)
# # mi_tuple = 1,2,3,4
# print(type(mi_tuple))
# t= (5,5.6,'fa',(10,20))
# print(t)
# print(t[3][0])
#
# mi_tuple = list(mi_tuple)
# print(mi_tuple)
#
# t = (1,2,3,1)
# r,x,y,z = t # tiene que tener la misma cantidad de elementos  listas y dic pueden hacer esto
#
# print(x,y,z)
# print(t.count(1))
#


# ##### SET son como los diccionarios al declarar pero los elementos no se repiten y los valores son unicos, no se muestras por indicen
# sus elementos son inmutables , no se pueden inclur listas i diccionarios en ssets

# mi_set = set([1,2,3,4,5])
# mi_set = {1, 2, 3, 4, 5}
# print(type(mi_set))
# print(mi_set)
#
# otro_set = {1,2,3}
# print(type(otro_set))
# print(otro_set)
# # print(otro_set[1]) #no
# print(len(mi_set))
# print(2 in mi_set)
#
# # union de sets
# s1= {1,2,3,4,5,6,7}
# s2={3,4,5}
# s3= s1.union(s2)
# print(s3)
# s1.add(2)
# # s1.remove(2)
# # s1.discard(2)
# s1.discard(26)
# s1.pop() #elimina el primer
# s1.clear() #elimina el primer
# print(s1)


#####   BOOLEANOS solo false y true como todos los demas lenguajes, capitalizado
# var1 = True
# var2 = False
#
# print(type(var1))
# print(var1)
#
# # numero = bool()
# numero = [1,2,3,4]
# control = 5 in numero
# print(type(control))
# print(control)
# val = None

#Proyecto del dia
# Crear un programa que primero le pida al usuario que
# ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
# poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
# letras a su elección y a partir de ese momento nuestro código va a procesar esa información
# para hacer cinco tipos de análisis

frase = input('Ingrese un texto cualquierda a su eleccion( Parrafo, frase ): ')
# frase ="Lorem Ipsum is a simply dummy text of the printing and typesetting industry b c Python"
letras = input('Ingresa 3 letras a tu eleccion juntas sin espacios: ')

letras = list(letras)
bool_to_text = {True:"Si", False: "No"}
# print(frase)
# print(letras)
print(f'Hay un numero de la primera letra en la frase: {frase.count(letras[0])}')
print(f'Hay un numero de la primera letra en la frase: {frase.count(letras[1])}')
print(f'Hay un numero de la primera letra en la frase: {frase.count(letras[2])}\n')
total_palabras = frase.split(' ')
# print(total_palabras)
print(f'El total de palabras en tu frase es: {len(total_palabras)}')
reversa = frase[::-1]
reversaPalabras = frase.split(' ')
reversaPalabras.reverse()
newR = reversaPalabras
# print(newR)
# conjunto = ' '.join(reversaPalabras)
print(f'La primera letra de la frase: {frase[0]} y la ultima es: {frase[-1]}')
print(f'El texto al reves quedaria asi: {reversa}\n y por palabras quedaria: \n {' '.join(newR)}')

print(f'La palabra Python se encuentra en el texto? {bool_to_text['Python' in frase]}')
# print()