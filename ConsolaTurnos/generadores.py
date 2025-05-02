# #cuidan el espacio de memomria del ordenador, esperan hasta que lo vuelvas a pedir - yield en vez de return
#
# # def mi_funcion():
# #     return 4
# def mi_funcion():
#     lista = []
#     for x in range(1,5):
#         lista.append(x*10)
#     return  lista
#
#
# # def mi_generador():
# #     yield 4
# def mi_generador():
#     for x in range(1, 5):
#         yield x * 10
#
# print(mi_funcion())
# print(mi_generador()) ## aqui solo lo guarda
#
# g= mi_generador()
#
# print(next(g))
# print(next(g)) # funciona mas con listar
#


def mi_generador():
    x = 1
    yield x

    x += 1
    yield x # lo produce cuando lo llamas

    x += 1
    yield x


g = mi_generador()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
