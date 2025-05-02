#son como siwtch, poder apagarlas o prender las funciones

def cambiar_letras(tipo):
    def mayusculas(text):
        print(text.upper())

    def minusculas(text):
        print(text.lower())

    if tipo == 'may':
        return mayusculas
    elif tipo == 'min':
        return minusculas

operacion = cambiar_letras('may')

operacion('min')
# mi_funcion = mayusculas
#
# mi_funcion('python')

# def una_funcion(funcion):
#     return funcion
#
# una_funcion(mayusculas('Probando'))

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

@decorar_saludo #esto son los  decoradores
def mayusculas_p(text):
    print(text.upper())


@decorar_saludo
def minusculas_p(text):
        print(text.lower())


mayusculas_p('Python')