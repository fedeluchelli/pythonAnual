# cadena1 = "python"

# SELECCIONAR
# print(cadena1[1])

# SLICING
# el primero aparece siempre
# print(cadena1[1:4:2])

# CAMBIAR LETRA
# palabra = "palavra"
# palabra[4] = "b"
# esto no se puede hacer
# la manera correcta es hacer un slicing
# palabra = palabra[0:4] + "b" + palabra[5:]
# print(palabra)

#1 DESAFÍO NUMEROS DE EQUIPOS

# win = 3
# tie = 1
# lose = 0
# ganados = int(input("Ingrese la cantidad de partidos ganados: "))
# empatados = int(input("Ingrese la cantidad de partidos empatados: "))
# perdidos= int(input("Ingrese la cantidad de partidos perdidos: "))
# total = int(ganados)*win + int(empatados)*tie + int(perdidos)*lose
# print(total)
# print(int(ganados)*3 + int(empatados) + int(perdidos)*0)
# totalPuntos = ganados*3 + empatados + perdidos*0
# print("Puntos totales: " + str(totalPuntos))
# optimizado
# print("\nPartidos ganados: " + str(ganados) + "\nPartidos empatados: " + str(empatados) + "\nPartidos perdidos: " + str(perdidos) + "\n\nPuntos totales: " + str(ganados*3+perdidos*0+empatados))

#2 DESAFÍO STRING

# cadena_1 = "versátil"
# cadena_2 = "Python"
# cadena_3 = "es un lenguaje"
# cadena_4 = "de programación"
# texto = cadena_2 + " " + cadena_3 + " " + cadena_4 + " " + cadena_1
# print(texto)

#3 DESAFÍO SLICING

# cadena1 = "neuqueN"
# # para dar vuelta  [::-1]
# cadena_volteada = cadena1[::-1]
# print(cadena_volteada)

# num1 = "12"
# num_volteado = num1[::-1]
# print(num_volteado)

# cadena = "acitametaM,5.8,otipeP,ordeP"
# cadena_formateada = cadena[::-1]
# print(cadena_formateada)


# materia = cadena_formateada[19:]
# nota = cadena_formateada[14:17]
# apellido = cadena_formateada[6:12]
# nombre = cadena_formateada[0:5]

# print("Nombre: " + nombre + "\nApellido: " + apellido +"\nNota: " + nota + "\nMateria: " + materia)

# cadena_separada = cadena_formateada.split(',')
# nombre = cadena_separada[0]
# apellido = cadena_separada[1]
# nota = cadena_separada[2]
# materia = cadena_separada[3]

# print("nombre: " + nombre + "\napellido: " +apellido+"\nmateria: "+materia+"\nnota: "+nota)

# INPUT
# nombre = input("ingrese nombre: ")
# print(nombre)

# OPERACIONES ARITMÉTICAS
# a=2
# b=4
# c=a*b
# print(c)
# cadena = "Python"
# print(cadena*2)

# PRIMER PROGRAMA EN PYTHON

# Promedio pesado: (13.3 + 2.10)/15. El peso que de 3 es 13, mientras que el de 10 es 2.
# el 3 es más importante

nota_1 = float(input("ingrese nota 1: "))
nota_2 = float(input("ingrese nota 2: "))
nota_3 = float(input("ingrese nota 3: "))

porcentaje_1 = 0.20
porcentaje_2 = 0.30
porcentaje_3 = 0.50

promedio = (nota_1*porcentaje_1) + (nota_2*porcentaje_2) + (nota_3*porcentaje_3)

print("La nota final es:", promedio) 
