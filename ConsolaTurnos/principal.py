from os import system

from paquete_numeros.numeros import *

def empezar():
    print(f'Bienvenido a la Farmacia G.'
          f'Seleccione a la area a dirigirse:\n'
          f'[1] - Perfumeria\n'
          f'[2] - Farmacia\n'
          f'[3] - Cosmeticos\n'
          f'[4] - Finalizar Programa'
          )

def start_program():
      empezar()
      departamento = int(input('Seleccione la opcion deseada: '))
      while True:
          try:
              departamento
          except ValueError:
              print('la opcion elegida no es un numero. Intente de nuevo')
          else:
              system('cls')
              break
      turno_dado(departaments[departamento], p)
    # perfumeria\
    # cosmetico
    # farmacia

start_program()