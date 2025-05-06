from os import system
from paquete_numeros.numeros import *

departaments_number = {
    1:p,
    2:f,
    3:c
}


def empezar():
    print(f'Bienvenido a la Farmacia G.'
          f'Seleccione a la area a dirigirse:\n'
          f'[1] - Perfumeria\n'
          f'[2] - Farmacia\n'
          f'[3] - Cosmeticos\n'
          f'[4] - Finalizar Programa'
          )

def start_program():

        looper = True
        while looper:
            empezar()
            try:
                departamento = int(input('Seleccione la opcion deseada: '))
            except ValueError:
                print('la opcion elegida no es un numero. Intente de nuevo')
            else:
                if 0 < departamento < 4 :
                    system('cls')
                    turno_dado(departaments[departamento], departaments_number[departamento])
                else:
                    looper = False
                    print('Adios!!')
                    break



start_program()