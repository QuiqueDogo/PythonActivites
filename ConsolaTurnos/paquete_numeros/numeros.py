
departaments = {
    1:'P-',
    2:'F-',
    3:'C-'
}


#decorador
def decorar_turno(funcion):

    def texto_decorado(dep, turno):
        # print(numero_generado, funcion, funcion(turno))
        print(f'---Aguarde y será atendido--\n'
              f'----- SU TURNO ES ----------')
        funcion(dep,turno)
        print(f'--------------------------')
    return  texto_decorado

@decorar_turno
def turno_dado(departamento, numero):
    print(f'----------  {departamento}{print(next(numero))}  -----------')


#generador
def generador_numero(depart):
    p=0
    f=0
    c=0
    while True:
        if depart == 1:
            p += 1
            yield p
        elif depart == 2:
            f += 1
            yield f
        elif depart == 3:
            c += 1
            yield c


p = generador_numero(1)
# print(next(p))
f = generador_numero(2)
# print(next(f))
c = generador_numero(3)
# print(next(c))
# print(next(perfumeria))
# print(next(farmacia))
# print(next(farmacia))
# print(next(cosmetico))
# print(next(cosmetico))
# print(next(cosmetico))

# turno_dado(departaments[2],6 )



