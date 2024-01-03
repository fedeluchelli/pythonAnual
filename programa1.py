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

# DESAFÍO NUMEROS DE EQUIPOS

# win = 3
# tie = 1
# lose = 0
ganados = int(input("Ingrese la cantidad de partidos ganados: "))
empatados = int(input("Ingrese la cantidad de partidos empatados: "))
perdidos= int(input("Ingrese la cantidad de partidos perdidos: "))

# total = int(ganados)*win + int(empatados)*tie + int(perdidos)*lose
# print(total)
# print(int(ganados)*3 + int(empatados) + int(perdidos)*0)
# totalPuntos = ganados*3 + empatados + perdidos*0
# print("Puntos totales: " + str(totalPuntos))

# optimizado
print("\nPartidos ganados: " + str(ganados) + "\nPartidos empatados: " + str(empatados) + "\nPartidos perdidos: " + str(perdidos) + "\n\nPuntos totales: " + str(ganados*3+perdidos*0+empatados))


