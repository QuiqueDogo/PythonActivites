##Metodos ayuda y doc
#
# dic = {'clave1':100, 'clave2':500}
#
# a = dic.popitem()
#
# print(a)
# print(dic)
#
# a=",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
# b = a.lstrip(',:%_#%_ _')
# print(a)
# print(b)
#
# frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
# frutas.insert(3,'naranja')
# print(frutas)
#
# marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
#
# marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
#
# conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
# print(conjuntos_aislados)
#
# ## funciones
#
# def saludar_persona(nombre):
#     '''
#     esta funcion se encargara de imprimir un saludo
#     '''
#     print('hola ' + nombre)
#
# saludar_persona('Luis')
#
# ## return
#
# def sumar(n1,n2):
#     return n1+n2
#
# print(sumar(1,2))
#
# def multiplicar(n1,n2):
#     total = n1 * n2
#     return total
#
# resultado = multiplicar(5,10)
#
# print(resultado)
#
#
# def chequear_3_cifras(numero):
#     return numero in range(100,1000)
# suma = 586+402
#
# resultado = chequear_3_cifras(suma)
# print(resultado)
#
# def chequear_3_cifras(lista):
#     for n in lista:
#         if n in range(100,1000):
#             return True
#         else:
#             pass
#     return False
#
# resultado = chequear_3_cifras([555,99,600])
#
# print(type(resultado))
# print(resultado)
# def chequear_3_cifras(lista):
#     lista_3_cifras = []
#     for n in lista:
#         if n in range(100,1000):
#             lista_3_cifras.append(n)
#         else:
#             pass
#
#     return lista_3_cifras
#
# resultado = chequear_3_cifras([555,99,600])
#
# print(type(resultado))
# print(resultado)
#
#
# def todos_positivos(lista):
#     for n in lista:
#         if n > 0:
#             pass
#         else:
#             return False
#     return True
#
#
# lista_numeros = [1, 23, 4, -45, -98, 16]
# print(todos_positivos(lista_numeros))
#
#
# def cantidad_pares(lista):
#     n_pares = 0
#     for n in lista:
#         if n % 2 == 0:
#             n_pares += 1
#         else:
#             pass
#     return n_pares
#
#
# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 16]
#
# print(cantidad_pares(lista_numeros))

# precios_cafe = [('capuchino', 1.5), ('expreso',2.5), ('moka',1.9)]

# for cafe,precio in precios_cafe:
#     print(cafe)
# for cafe,precio in precios_cafe:
#     print(precio * .45)
#
#
# def cafe_mas_caro(lista_precio):
#     precio_mayor =0
#     cafe_caro = ''
#
#     for cafe,precio in lista_precio:
#         if precio > precio_mayor:
#             precio_mayor = precio
#             cafe_caro = cafe
#         else:
#             pass
#
#     return (cafe_caro, precio_mayor)
#
# cafe, precio = cafe_mas_caro(precios_cafe)
#
# print(f"El cafe mas caro es: {cafe} cuyo precio es: {precio}")

## funcion para tomar el palito mas grande

# from random import shuffle
# #LISTA INICIAL
# palitos = ['-','--','---','----']
#
# #MEZCLAR PALITOS
# def mezclar(lista):
#     shuffle(lista)
#     return lista
#
# #PEDIRLE INTENTO
# def probar_suerte():
#     intento = ''
#
#     while intento not in ['1',"2",'3','4']:
#         intento = input('Elige un numero del 1 al 4: ')
#
#     return int(intento)
#
# # intento1 = probar_suerte()
# # print(intento1)
# #COMPROBAR INTENTO
#
# def chequear_intento(lista,intento):
#     if lista[intento - 1] == '-':
#         print('A lavar los platos')
#     else:
#         print('Te has salvado')
#
#     print(f"te ha tocado {lista[intento-1]}")
#
# palitos_mezclados = mezclar(palitos)
# seleccion = probar_suerte()
# chequear_intento(palitos_mezclados, seleccion)


# from random import choice
#
# dados = list(range(1, 7))
#
#
# def lanzar_dados():
#     primer = choice(dados)
#     segundo = choice(dados)
#     # print([primer, segundo])
#     return [primer, segundo]
#
#
# pri, seg = lanzar_dados()
#
#
# def evaluar_jugada(uno, dos):
#     suma_dados = uno + dos
#     if suma_dados <= 6:
#         return f'La suma de tus dados es {suma_dados}. Lamentable'
#     elif 6 < suma_dados < 10:
#         return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
#     elif suma_dados >= 10:
#         return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
#

# print(evaluar_jugada(pri, seg))
#
# lista_numeros=[1,2,3,8,9,10,3,5,4,4,5,6,7,8,6,7,9,0]
# def reducir_lista(lista):
#     nueva_lista = set(lista)
#     lista_denuevo = list(nueva_lista)
#     lista_denuevo.sort()
#     ordenada = lista_denuevo
#     ordenada.pop(-1)
#     return ordenada
#
# nuevo = reducir_lista(lista_numeros)
# print(nuevo)
#
# lista_numeros = [1, 2, 3, 8, 9, 10, 3, 5, 4, 4, 5, 6, 7, 8, 6, 7, 9, 0]
#
#
# def reducir_lista(lista):
#     nueva_lista = set(lista)
#     lista_denuevo = list(nueva_lista)
#     lista_denuevo.sort()
#     ordenada = lista_denuevo
#     ordenada.pop(-1)
#     return ordenada
#
#
# nuevo = reducir_lista(lista_numeros)
# lista_guardada = reducir_lista(lista_numeros)
#
#
# def promedio(lista_save):
#     suma = 0
#     prom = len(lista_save)
#     for n in lista_save:
#         suma += n
#     return suma / prom
#
# calculo = promedio(lista_guardada)
# print(calculo)

#
# moneda = ['Cara', 'Cruz'];
# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# from random import choice
#
#
# def lanzar_moneda():
#     resultado = choice(moneda)
#     return resultado
#
#
# lanzamiento = lanzar_moneda()
#
#
# def probar_suerte(dado, lista):
#     newlista = lista
#     if dado == 'Cara':
#         print("La lista se autodestruirá")
#         newlista = []
#         return newlista
#     elif lanzamiento == 'Cruz':
#         print("La lista fue salvada")
#         return newlista
#
#
# probar_suerte(lanzamiento, lista_numeros)
# print(probar_suerte(lanzamiento, lista_numeros))


# ## ARGUMENTOS INDEFINIDOS (*args) (**kwargs)
#
# def suma(*args): ##astericos despues de los argumentos
#     # print(args)
#     # total = 0
#     # for arg in args:
#     #     total += arg
#     # return total
#     return sum(args)
#
# print(suma(5,6,5,1,10,500))

# def suma(**kwargs):
#     print(kwargs) ##diccionario
#
# suma(x=3,y=5,z=2)
# def suma(**kwargs):
#     total = 0
#     for clave, valor in kwargs.items():
#         print(f'{clave} es igual a {valor}')
#         total += valor
#     return total
#
# print(suma(x=3,y=5,z=2))
#
# def prueba(num1,num2,*arg, **kwargs): ## **tuplas y listas
#     print(f'el primer valor es {num1}')
#     print(f'el segundo valor es {num2}')
#     print(len(kwargs))
#     for ar in arg:
#         print(f'arg = {ar}')
#
#     for clave, valor in kwargs.items():
#         print(f'{clave} es igual a {valor}')
#         # total += valor
#     # return total
# args = [100,200,400]
# kwargs1= {'x':'iuno','y':'dos','z':'tres'}
# prueba(15,50,*args, **kwargs1)
#
# def lista_atributos(**kwargs):
#     lista = []
#     for clave, valor in kwargs.items():
#         lista.append(valor)
#     return lista
#
# print(lista_atributos(**kwargs1))
#
#
# def describir_persona(nombre, **kwargs):
#     print(f'Características de {nombre}:')
#     for nombre_argumento, valor_argumento in kwargs.items():
#         print(f'{nombre_argumento}: {valor_argumento}')
#
#
# funcion = describir_persona("María", color_ojos="azules", color_pelo="rubio")
# print(funcion)

#
# def devolver_distintos(*args):
#     newlista = list(args)
#     newlista.sort()
#     suma_total = 0
#
#     for arg in args:
#         suma_total += arg
#     if suma_total >= 15:
#         return max(newlista)
#     elif suma_total < 10:
#         return min(newlista)
#     elif 10 < suma_total < 15:
#         return newlista[1]
#
# print(devolver_distintos(7,2,4))
#
# def palabras_unicas(palabra):
#     separadas = list(palabra)
#     unicas = set(separadas)
#     unicas = list(unicas)
#     unicas.sort()
#     print(unicas)
#
# palabras_unicas('entretenido')
# palabras_unicas('cascarabias')
#
# def repetidos_numeros(*args):
#     contador = 0
#
#     for num in args:
#         if contador + 1 == len(args):
#             return False
#         elif args[contador] == 0 and args[contador+1] == 0:
#             return True
#         else:
#             contador +=1
#     return False
#
# print(repetidos_numeros(0,6,8,5,0,5,6,4,0,1,5,3,6,5,0))
#
# def contar_primos(num):
#     conteo = []
#     for i in range(2, num + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             print(f"{i} es primo")
#             conteo.append(i)
#     print(conteo)
#     return len(conteo)
#
# print(contar_primos(50))


#choice
#  pedir letra, validar letra, chequear letra, ver si gano

from random import choice
from time import sleep



palabras = ['gato','perro','perico','leon','cocodrilo','murcielago','cucaracha']
palabra_seleccionada = choice(palabras)
vidas=6
def palabra_guiones(palabra):
    letras = []
    for p in palabra:
        letras.append('_')
    letras = ''.join(letras)
    return letras

guiones = palabra_guiones(palabra_seleccionada)

abecedario =''
for i in range(26):
    abecedario = abecedario + (chr(ord('a') + i))
print(f'Bienvenido al juego del Ahorcado, por favor sigue las instrucciones para jugar. Tienes 6 vidas.\n'
      f'La categoria es animales. '
      f'La palabra secreta tiene {len(guiones)} letras \n'
      f'{guiones}')

def validar_letra(letra):
    ingreso = letra
    while ingreso not in abecedario:
        ingreso = input('Por favor elige una palabara del abecedario')
    return ingreso

def validar_len(letra):
    ingreso = letra
    while len(ingreso) != 1:
        ingreso = input('Solo se puede escoger una letra. Por favor seleccione solo una: ')
    return ingreso

lista_erronea = []
lista_buena = guiones

def guiones_por_palabras(letra, seleccionada ,lista):
    contenido = list(lista)
    seleccionada = list(seleccionada)

    for i,p in enumerate(seleccionada):
        if p == letra: contenido[i] = letra


    return contenido

def recorrer_palabra(letra):
    atino = False
    buena = lista_buena
    if letra in palabra_seleccionada:

        buena = guiones_por_palabras(letra, palabra_seleccionada, lista_buena)
        atino = True
    else:
        print('La letra seleccionada no esta en la palabra secreta\n')
        lista_erronea.append(letra)

    return lista_erronea,buena, atino

while vidas > 0:
    incorrectas = []
    letras = ''
    if vidas != 6:
        print(f'Aun quedan {vidas} vidas')
        for p in lista_erronea:
            incorrectas.append(p.upper())
        letras = '-'.join(incorrectas)
        print(f'Estas son las letras que has usado: {letras}')

    ingreso_letra = input('Ingresa una letra ')
    ingreso_letra = validar_len(ingreso_letra) #validamos longitud
    ingreso_letra = validar_letra(ingreso_letra) #validamos que este en el abecedario

    no,si,atino = recorrer_palabra(ingreso_letra)
    lista_buena = si

    palabra_cambiada = []
    for p in si:
        palabra_cambiada.append(p)
    palabra_cambiada = ''.join(palabra_cambiada)
    print(f'\nLa palabra es: {palabra_cambiada}')
    if not atino:
        vidas -= 1
    if '_' not in palabra_cambiada:
        print('Ganaste en el juego del Ahorcado')
        break

if vidas == 0:
    print('Perdiste en el juego del Ahorcado')



