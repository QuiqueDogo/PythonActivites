# veremos operadores  de comparacion, logicos, control de flujo en py, loops, rangos, enumeradores, zip, random etc
#### OPERADORES DE COMPARACION
# == igual a
# != diferente a
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que
#
# mi_variable = 'hola mundo'
# # mi_bool = 10==10
# # mi_bool = 'Blanco'=='blanco'
# # mi_bool = 'Blanco'.lower()=='blanco'
# # mi_bool = 100.0 == 100
# # mi_bool = 100
# .0 != # mi_bool = 101 != 100
# # mi_bool = 100>99
# # mi_bool = 5 >= 5
# mi_bool = 7 >= 6 & 14 > 2
# print(mi_bool)

#
# #OPERADORES LOGICOS (and or not) & | !
# a=10
# b=5
# c=15
#
# # mi_bool = 4 < 5 < 6
# # mi_bool =( 4 < 5) and ( 5 < 6)
# # mi_bool =10 == 10  or 3 == 3
# # mi_bool = 1 == 10  or 3 == 3
# texto = 'esta frase es breve'
# mi_bool = ('frase' in texto) and ('breve' in texto)
# print(mi_bool)
#
#
#
#
##### CONTROL DE FLUJO  if HAY QUE RESPETAR LAS JERARQUIAS DE TABULACIONES
# if 10 < 9:
#     print('Es Correcto')
# else:
#     print('No ta chido')

# mascota = 'perro'
# if mascota == 'gato':
#     print('Tienes un gato')
# elif mascota == 'perro':
#     print('Tienes un perro')
# else:
#     print('No se que animal es')

# edad = 16
# calificacion = 9
# if edad < 18:
#     print('Eres menor de edad')
#     if calificacion >= 7:
#         print('Aprobado')
#     else:
#         print('No Aprobado')
# else:
#     print('Eres adulto')

# ### Loops For - While ( listas )
#
# nombres = ['pablo','laura','fede','luis', 'julia']
# listas = ['a','b','c','d']
# for element in nombres:
#     print(f'Hola {element}')
# for letra in listas:
#     numero_letra = listas.index(letra) #indece
#     print(f'Letra {numero_letra} : letra')
# for nombre in nombres:
#     if nombre.startswith('l'):
#         print(nombre)
#
# numeros = [1,2,3,4,5]
# mi_valor = 0
# for numero in numeros:
#     mi_valor = mi_valor + numero
#     # print(mi_valor) ## no dejar al mismo nivel del for
#
# print(mi_valor) ## 15
#
# palabra = 'python'
# for letra in palabra:
#     print(letra)
# for letra in 'python':
#     print(letra)
#
# for a,b in [[1,2],[3,4],[5,6]]:
#     print(a)
#     print(b)
#
# dic = {'clave': 'a', 'clave2':'b','clave3':'c'}
# for elemento in dic:
#     valor = dic[elemento]
#     print(f'{elemento} con valor: {valor}')
#
# dic = {'clave': 'a', 'clave2':'b','clave3':'c'}
# for elemento in dic.items():
#     print(f'{elemento}')
#
# for elemento in dic.values():
#     print(f'{elemento}')
#
# for a,b in dic.items():
#     print(f'{a} y {b}')
#
#
#

#### WHILE
# monedas = 5
# while monedas > 0:
#     print(f'Tengo {monedas} monedas') #loop infinito
#     # monedas = monedas - 1 # para el loop infinito
#     monedas -= 1 # forma corta de restar
# else:
#     print('No hay lana')
#
# print('xd')

# respuesta = 's'
# while respuesta == 's':
#     respuesta = input('Quieres seguir? (s/n)')
# else: print('Gracias')

# Pass

# respuesta = 's'
# while respuesta == 's':
#     # pass
#     break
#
#
# print('Hola')

###BREAK
# nombre = input('Tu nombre: ')
# for letra  in nombre:
#     if letra == 'l':
#         break
#     print(letra)
#
# ## CONTINUE
# nombre = input('Tu nombre: ')
# for letra  in nombre:
#     if letra == 'l':
#         continue
#     print(letra)

# numero = 10
# while numero <= 10 and numero >= 0:
#     print(numero)
#     numero -= 1
# numero = 50
# while 50 >= numero >= 0:
#     # print(numero)
#     if numero % 5 == 0:
#         print(numero)
#     elif numero % 5 != 0:
#         pass
#     numero -= 1


##### RANGE (no recibe floats)

# for numero in range(5):
#     print(numero)
# print("\n")
# for numero in range(5,9):
#     print(numero)
# print("\n")
# for numero in range(20,30):
#     print(numero)
# for numero in range(20,31,3):
#     print(numero)

# lista = list(range(1,101))
# print(lista)


# ### ENUMERADORES ( indice, elemento)
#
# lista = ['a','b','c']
# mis_taples = list(enumerate(lista))
# print(mis_taples[1][0])
#
# indice = 0
# for item in enumerate(lista):
#     print(indice, item)
#     indice += 1
#
# for a, b in enumerate(lista):
#     print(a, b)
#
# for indice1, item in enumerate(range(50,55)):
#     print(indice1, item)

# ####  ZIP union de listas en tuples
# nombres = ['Ana', 'Hugo','Valeria']
# edades = [65,29,42,55,555]
# ciudades = ['Lima','Madrid','Mexico', 'XD']
#
# combinados = zip(nombres, edades, ciudades)
# print(combinados)
# combinados = list(zip(nombres, edades, ciudades))
# print(list(combinados))
#
# for nombre,edad,ciudad in list(combinados):
#     print(f'{nombre} tiene {edad} anios y vive en {ciudad}')

# ###### MIN Y MAX
#
# minimo = min(58,96,72,64,35)
# maximo = max(58,96,72,64,35)
#
# print(minimo )
# print(maximo )
#
# lista = [58,96,72,64,35]
# print(max(lista))
# print(f'El menos es {min(lista)}  y el mayor es {max(lista)}')
#
# # En textos EL MIN  busca primero por mayuscular
# nombre = 'CarlOs'
# print(min(nombre.lower()))
#
# dic = {'C1':45, 'C2':11}
# print(min(dic.values()))

### RANDOM

# from random import randint, uniform, random, choice, shuffle  #se puede importar todos agregando '*'
#
# aleatorio = randint(1,50)
# print(aleatorio)
# aleatorio1 = round(uniform(0.0, 100.0),2)
# print(aleatorio1) ##aleatorio con floats
#
# aleatorio2 = random()
# print(aleatorio2) ##float menos de 1
#
# colores = ['azul','verde','rojo','amarillo']
# aleatorio3 = choice(colores)
# print(aleatorio3)
#
# numeros  = list(range(5,50,5))
# print(numeros)
# shuffle(numeros) # no se almacena en lista, no se aplica a inmutables
# print(numeros)

# ### COMPRENSION DE LISTAS
# palabra = 'python'
# lista = []
#
# for letra in palabra:
#     lista.append(letra)
# print(lista)
#
# ## forma corta
# lista = [letra for letra in palabra]
# lista = [ff for ff in palabra]
# lista = [n for n in range(0,21,2)]
# lista = [n/2 for n in range(0,21,2)]
# lista = [n for n in range(0,21,2) if n*2 > 10]
# lista = [n if n*2 > 10 else 'no' for n in range(0,21,2) ]
# print(lista)
#
# ## hay que hacer buen legibilidad
# pies = [10,20,30,40,50]
# metro = [round(p/3.281, 2) for p in pies]
# print(metro)
#
#
# valores = [1, 2, 3, 4, 5, 6, 9.5]
# valores_pares = [val for val in valores  if val%2 == 0]
# print(valores_pares)


####MATCH

serie = 'N-02'

# if serie == 'N-01':
#     print('Samsung')
# elif serie == 'N-02':
#     print('Nokia')
# elif serie == 'N-03':
#     print('Motorola')
# else:
#     print('No existe')
#
## ahora con match
#
# match serie:
#     case 'N-01':
#         print('Samsung')
#     case 'N-02':
#         print('Nokia')
#     case 'N-03':
#         print('Motorola')
#     case _:
#         print('No existe')
#
# cliente = {'nombre':'Federico',
#            'edad':45,
#            'ocupacion': 'instructor'}
#
# pelicula = {'titulo':'Matrix',
#             'ficha_tecnica':{'protagonista':'Keanu reeves',
#                              'director':'Lana y lilly wachowski'}}
#
# elementos = [cliente, pelicula, 'libro']
#
# ## aqui lo arreglos que esstan en case,detectan patrones deben tener la misma estructura para poder cacharlo, switch
# for e in elementos:
#     match e:
#         case {'nombre': nombre,
#               'edad':edad,
#               'ocupacion':ocupacion}:
#             print('Es un cliente')
#             print(nombre, edad, ocupacion)
#         case {'titulo':titulo,
#               'ficha_tecnica':{'protagonista':prota, 'director':directo}}:
#             print('Es una pelicula')
#             print(titulo, prota, directo)
#         case _:
#             print('No se que es esto')

from random import randint

nombre = input('Cual es tu nombre? ')
print(f'Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos'
      f'para adivinar cuál crees que es el número(Solo ingresar numeros)')

n_intentos = 8
aleatorio = randint(1,101)
# print(aleatorio)

while 0 < n_intentos <= 8:
    print(f'\nNo Intentos disponibles: {n_intentos}')
    numero_ingresado = input('Escoge tu numero: ')
    try:
        if 0 <= int(numero_ingresado) <= 100:
            if int(numero_ingresado) == aleatorio:
                print('\nGanaste. Adivinaste el numero')
                break
            elif int(numero_ingresado) > aleatorio:
                print('Incorrecto,  has elegido un número mayor al número secreto.')
            elif int(numero_ingresado) < aleatorio:
                print('Incorrecto,  has elegido un número menor al número secreto.')
        else:
            print('El numero que seleccionaste esta fuera del rango de 1-100')
    except:
        print('Lo que escribiste NO es un numero')

    n_intentos -= 1
    if n_intentos == 0:
        n_intentos = 8
        print('Intentaremos de nuevo 8 veces hasta q ganes')

