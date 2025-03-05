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

edad = 16
calificacion = 9
if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('No Aprobado')
else:
    print('Eres adulto')