# mas sobre os y shutil
# import os
#
# # print(os.getcwd())
# archivo = open('cursor.txt', 'w')
# archivo.write('Textp de Prueba')
# archivo.close()
#
# print(os.listdir())
#
# import shutil
#
# # # shutil.move('cursor.txt', 'C:\\Users\\Luis\\') ## mover archios os.rm remover carpeta, shutil.mrtree elimana todooo y recursivo
# #
# # import send2trash
# # send2trash.send2trash('C:\\Users\\Luis\\python\\BuscadorNumeroSerie\\cursor.txt')
#
# import os
#
# # print(os.walk('C:\\Users\\Luis\\python'))
#
# ruta = 'C:\\Users\\Luis\\python'
#
# for carpeta, subcarpeta, archivo in os.walk(ruta):
#     print(f'en la carpeta: {carpeta}')
#     print(f'las subcarpetas son: {carpeta}')
#     for sub in subcarpeta:
#         print(f'\t{sub}')
#     print(f'Los archivos son')
#     for arch in archivo:
#         if arch.startswith('p'):
#             print(f'\t{arch}')
#
#     print('\n')


import datetime

mi_hora = datetime.time(17,10,59)
print(mi_hora)
