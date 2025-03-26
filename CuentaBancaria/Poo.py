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

class Pajaro:

    alas = True # estos son de clasa

    def __init__(self, color, especie): # Metodo constructor, lo que requiere self representa la instancia del objecto que creamos
        #
        self.color = color # atributos de la clase que definimos
        self.especie = especie

mi_pajaro = Pajaro('azul','tucan')
print(f'Mi pajaro es de color {mi_pajaro.color} y es un {mi_pajaro.especie}')
print(Pajaro.alas)
print(mi_pajaro.alas)