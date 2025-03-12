mi_archivo = open('Prueba.txt')
# print(mi_archivo.read()) ## para ver contenido
una_linea = mi_archivo.readline() ## lee la primera y luego se salta a la siguiente
# print(una_linea)
print(una_linea.rstrip()) ## para eliminar el salto de linea
una_linea = mi_archivo.readline()
print(una_linea)
una_linea = mi_archivo.readline()
print(una_linea)
# una_linea = mi_archivo.readlines()
# print(una_linea)

# print(mi_archivo.readline()) ## para primera linea
# print(mi_archivo.readlines(-1)) ## para primera linea
# mi_archivo.read()










mi_archivo.close() ## siempre cerrar archivo

