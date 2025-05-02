#decorador
def decorar_turno(funcion):

    def texto_decorado(turno):
        # print(numero_generado, funcion, funcion(turno))
        print(f'---Aguarde y será atendido--\n'
              f'----- SU TURNO ES ----------')
        funcion(turno)
        print(f'--------------------------')
    return  texto_decorado

@decorar_turno
def turno_dado(numero):
    print(f'------------{numero}------------')

#generador
turno_dado(6)



