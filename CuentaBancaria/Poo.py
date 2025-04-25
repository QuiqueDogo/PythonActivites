# POO o OOP
# clase , objectos a representar, pajaros,
# atributos. color, tipo, habitad, edad
# metodos, volar, comer,

# class Pajaro:
#     pass
#
# mi_pajaro = Pajaro()
# otro_pajaro = Pajaro()
#
# print(mi_pajaro)
# print(otro_pajaro)
# print(type(mi_pajaro))


#  Atributos, atributos de clase, tambien hay de instancia
# instancia

# class Pajaro:
#
#     alas = True # estos son de clasa
#
#     def __init__(self, color, especie): # Metodo constructor, lo que requiere self representa la instancia del objecto que creamos
#         #
#         self.color = color # atributos de la clase que definimos
#         self.especie = especie
#
# mi_pajaro = Pajaro('azul','tucan')
# print(f'Mi pajaro es de color {mi_pajaro.color} y es un {mi_pajaro.especie}')
# print(Pajaro.alas)
# print(mi_pajaro.alas)

# Metodos para una clase, init es un metodo especial

# class Pajaro:
#
#     alas = True # estos son de clasa
#
#     def __init__(self, color, especie): # Metodo constructor, lo que requiere self representa la instancia del objecto que creamos
#         #
#         self.color = color # atributos de la clase que definimos
#         self.especie = especie
#
#     def piar(self):
#         print('pio, mi color es {}'.format(self.color))
#
#     def volar(self, metros):
#         print(f'El pajaro ha volado una cantidad de {metros} metros')
#
# piolin = Pajaro('amarillo', 'canario')
#
# piolin.piar()
# piolin.volar(50)


# Decoradores - Metodos de instancia, metodos de clase @classmethod, metohs estaticos @staticmethod

# class Pajaro:
#
#     alas = True # estos son de clasa
#
#     def __init__(self, color, especie): # Metodo constructor, lo que requiere self representa la instancia del objecto que creamos
#         #
#         self.color = color # atributos de la clase que definimos
#         self.especie = especie
#
#     def piar(self):
#         print('pio')
#
#     def volar(self, metros):
#         print(f'El pajaro ha volado una cantidad de {metros} metros')
#         self.piar()
#
#     def pintar_negro(self):
#         self.color = 'negro'
#         print(f'Ahora el pajaro es {self.color}')
#
#     @classmethod
#     def poner_huevos(cls, cantidad): #no necesita una instancia para poder ejecutarse
#         print(f'Puso {cantidad} de huevos')
#         # print(f'Es de color {self.color}') # estos no pueden acceder a los atributos
#         cls.alas = False #solo a lso atributos de clase
#         print(Pajaro.alas)
#
#     @staticmethod #no se refieren a la clase o a la instancia, no se modifica nada
#     def mirar():
#         print('El pajaro mira')
#         # self.color= 'rojo' #no se puede
#         # cls.alas = 2 # tampoco
#
#
# piolin = Pajaro('amarillo', 'canario')
# # piolin.pintar_negro()
# # piolin.volar(80)
# piolin.piar()
# # piolin.alas = False
# # print(piolin.alas)
#
# #METODOS DE CLASE
#
# Pajaro.poner_huevos(3) # No necesitan una instancia para poder ejecutarse, estos no pueden acceder a los atributos
# # Pajaro.piar() # esto no se puede
# Pajaro.mirar()

#HERENCIA - puede usarse metodos en otras clases, en este caso se heredan
# class Animal:
#
#     def __init__(self,edad, color):
#         self.edad = edad
#         self.color = color
#
#     def nacer(self):
#         print('este animal ha nacido')
#
#
# class Pajaro(Animal):
#     pass
#
# piolin = Pajaro(2, 'negro')
# piolin.nacer()
# print(piolin.color)
#
# print(Pajaro.__bases__)
# print(Animal.__subclasses__())

#Herencia Extendida
# class Animal:
#
#     def __init__(self,edad, color):
#         self.edad = edad
#         self.color = color
#
#     def nacer(self):
#         print('este animal ha nacido')
#
#     def hablar(self):
#         print('Este animal emite un sonido')
#
#
# class Pajaro(Animal):
#
#     def __init__(self, edad, color, altura_vuelo):
#         super().__init__(edad, color) # se herada esta construccion
#         self.altura_vuelo = altura_vuelo
#
#     def hablar(self): #al tener metodos iguales, se sobreescribe en el que este si es que la herencia se llama igual
#         print('Pio')
#
#     def volar(self, metros):
#         print(f'El parajo vuela {metros} metros')
#
#
# # piolin = Pajaro(2, 'negro')
# piolin = Pajaro(2, 'negro', 10)
# mi_animal = Animal(5, 'azul')
#
# # piolin.nacer()
# # piolin.hablar()
# # piolin.volar(100)
#
# print(piolin.color)

#herencia multiple -- se transmite todoo

# class Padre:
#     def hablar(self):
#         print('Hola')
#
# class Madre:
#     def reir(self):
#         print('jajaja')
#
#     def hablar(self):
#         print('Que tal')
#
# class Hijo(Madre, Padre): # orden de funcion dependiendo de el orden de la herencia
#     pass
#
# class Nieto(Hijo):
#     pass
#
# mi_nieto = Nieto() #instancia de la clase nieto
# mi_nieto.hablar()
# mi_nieto.reir()
#
# print(Nieto.__mro__) #orden de resolucion de metodos


#Poliformismo - muchas formas, los objecctos pueden tomar diferentes formas
# objectos de diferentes clases, puedes compartir el mismo nombre de metodo.
#
# class Vaca:
#     def __init__(self, nombre): #constructor
#         self.nombre = nombre
#
#     def hablar(self):
#         print(self.nombre + ' dice muuu')
#
# class Oveja:
#     def __init__(self, nombre):  # constructor
#         self.nombre = nombre
#
#     def hablar(self):
#         print(self.nombre + ' dice beee')
#
# vaca1 = Vaca('aurora')
# oveja1 = Oveja('nube')
#
# # vaca1.hablar()
# # oveja1.hablar()
#
# animales = [vaca1, oveja1]
#
# for animal in animales: # llamar a cada uno de estos objectos pero ejecutando sus metodos de nombre igual
#     animal.hablar()
#
# def animal_habla(animal):
#     animal.hablar()
#
# animal_habla(vaca1)
# animal_habla(oveja1)


#Metodos especiales __nombre__, __init__
# mi_lista=[1,1,1,1,1,1]
# print(len(mi_lista))
#
# class Objecto:
#     pass
#
# mi_objeto = Objecto()
#
# print(mi_objeto)
#
#
# class CD:
#
#     def __init__(self, autor, titulo, canciones):
#         self.autor =autor
#         self.titulo = titulo
#         self.canciones = canciones
#
#     def __str__(self): #Nombrar el objecto a como quieres que se imprima,
#         return f'Album: {self.titulo} de {self.autor}'
#
#     def __len__(self): # metodos under
#         return self.canciones
#
#     def __del__(self):
#         print('Se ha eliminado el CD')
#
# mi_cd = CD('Pink floyd', 'The Wall', 24)
# print(mi_cd)
# print(len(mi_cd))
#
# del mi_cd

# print(mi_cd)

# Ejercicio Cuenta Bancaria, haremos que una persona pueda realizar operaciones a su cuenta bancaria

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, cuenta, balance:int, nombre, apellido):
        super().__init__(nombre, apellido)
        self.cuenta = cuenta
        self.balance = balance

    def __str__(self):
        return f'{self.nombre} {self.apellido} con numero de cuenta: {self.cuenta} tiene ${self.balance} disponible'

    def info(self):
        return f'{self.nombre} {self.apellido} con numero de cuenta: {self.cuenta} tiene ${self.balance} disponible'

    def depositar(self):
        monto = input('¿Cuanto deseas depositar?')
        self.balance += int(monto)
        print('\nMonto Depositado.')
        return f'Se Ha ingresado ${monto} a tu cuenta.'
        # self.__str__()

    def retirar(self):
        monto_retirado = int(input('¿Cual es el monto a retirado?'))
        res = self.balance - monto_retirado
        # print(res)
        if res < 0:
            return f'Saldo Insuficiente para retirar'
        else:
            return f'Se han retirado ${monto_retirado} de tu cuenta.'


print(f'Bienvenido al Banco. Por favor ingrese sus datos para comenzar:\n ')
Pcuenta = input('Ingresa tu numero de cuenta:')
Pbalance = input('Ingresa el balance inicial:')
Pnombre = input('Ingresa tu nombre:')
Papellido = input('Ingresa tu Apellido:')

nuevo_cliente = Cliente(Pcuenta, int(Pbalance),Pnombre,Papellido)
print(nuevo_cliente)
loop = True
funciones = {
    '1':nuevo_cliente.info,
    '2':nuevo_cliente.depositar,
    '3':nuevo_cliente.retirar,
}


while loop:
    print(f'\nPor favor elige una'
          f'de las siguientes opciones:\n'
          f'[1] - Consultar Informacion\n'
          f'[2] - Depositar\n'
          f'[3] - Retirar\n'
          f'[4] - Finalizar Programa'
          )
    paso = input('Seleccione una opcion: \n')
    if paso == '4':
        print('Hasta Pronto')
        break
    else:
        print(funciones[paso]())
