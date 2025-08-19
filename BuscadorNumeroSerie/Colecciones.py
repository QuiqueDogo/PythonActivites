# from collections import Counter
#
# # numeros = [8,6,5,9,8,85,5,4,4,1,2,3,44,6,9,798,4,58,1,2,5]
# frase = 'al pan pan y al vino vino'
# # print(Counter(numeros))
# print(Counter(frase))
# print(Counter('missisipi'))
#
# serie = Counter([1,1,1,1,1,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2])
#
# print(serie.most_common())
# print(serie.most_common(2))
# print(list(serie))

# from collections import defaultdict
#
# # mi_dic = {'uno':'verde', 'dos':'azul', 'tres':'rojo'}
# mi_dic = defaultdict(lambda: 'nada')
# mi_dic['uno'] = 'verde'
# print(mi_dic['dos'])
# print(mi_dic)

from collections import namedtuple


mi_tupla= (500,18,65)
print(mi_tupla[1])

Persona = namedtuple('Persona',['nombre', 'altura','peso']) #crea una tupla en fa en fa, casi como una calse
ariel = Persona('Ariel',1.76,79)

print(ariel.nombre)
print(ariel)
