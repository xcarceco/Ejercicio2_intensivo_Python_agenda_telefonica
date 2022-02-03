import os
diccionario = {}
file = open('/Users/xavi/Downloads/Agenda.txt','a')
nombre = input( "Ingrese nombre y apellido: \n")
telefono =input( "Ingrese el teléfono \n")
file.write(nombre)
file.write(' teléfono: ')
file.write(str(telefono))
file.write('\n')
diccionario = {nombre, telefono}
print(diccionario)
file.close()

diccionario = {nombre, telefono}

nombre = input("Ingresa búsqueda: ")
with open ('/Users/xavi/Downloads/Agenda.txt','r') as file:
    for line_number, line in enumerate(file,start=1):
        if nombre in line:
            print(line)