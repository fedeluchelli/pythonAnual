# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # LISTA # # # # # # # # # # # # # # # # # # # # # #

# mi_lista = ["e", 2, -11, "Fede", [5,4,8]]

# print(mi_lista[4])
# sub_lista = mi_lista[4]
# print(sub_lista[2])

# lista_agregada = mi_lista+[123,456,789]

# print(lista_agregada)
# lista_agregada[:4]=[]

# APPEND - agrega al último
# lista_agregada.append([123,1233,12333])
# lista_agregada[2:-4] =[]

# POP - elimina el último (salvo se designe ubicación a eliminar)
# lista_agregada.pop(1)
# print(lista_agregada)

# COUNT - cuenta el número de veces que se repite
# print(lista_agregada.count(2))

# INDEX - busca un ítem y dice la ubicación (error si no lo encuentra)
# print(lista_agregada.index(2))

# DESAFÍO LISTAS

# lista_1 = [1, 12, 123]
# lista_2 = ["Bye", "Ciao", "Agur", "Adieu"]
# lista_1.append(456789)
# lista_1.append("Hola Mundo!")
# print(lista_1)

# lista_2.append("Hola y Adios")
# lista_2.append(5555)
# print(lista_2)

# lista_1.pop()
# lista_3 = lista_1
# print(lista_3)

# eliminar el primer y último
# lista_2.pop(0)
# lista_2.pop(-1)
# lista_4 = lista_2

# seleccionar solo los del medio
# lista_4 = lista_2[1:-1]
# print(lista_4)

# lista_5 = lista_3 + lista_4
# print(lista_5)


# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # TUPLA # # # # # # # # # # # # # # # # # # # # # #
# como listas, pero no se pueden modificar

# mi_tupla = (1,2,3,4)
# print(mi_tupla)

# suporta todo tipo de datos, incluso otras listas
# se pueden modificar las listas que están dentro de la tupla? SÍ

# mi_tupla = (1,2,[1,2,3,4])
# print(mi_tupla)
# mi_tupla[2].append(5)
# print(mi_tupla)

# slicing Sí

# print(mi_tupla[1])
# mi_tupla_1 = mi_tupla[1]
# print(mi_tupla_1)
# mi_tupla_agregada = mi_tupla+(5,6,7,8)
# print(mi_tupla+(5,6,7,8,9))
# print(mi_tupla_agregada)

# ANIDACIÓN

# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]
# resultado = [a,b,c]
# print(resultado)
# # selecciona 'a'
# print("a: " , resultado[0])
# # selecciona '2' de 'a'
# print("a-2: ",resultado[0][1])
# print()

# TRANSFORMAR UNA COLECCIÓN EN OTRA
# convertir lista en tipla, o al revés
# transformado puedo tratarla como lista y luego volver a hacerla tupla
# numeros = (1,2,3,4)
# numeros_lista = list(numeros)
# numeros_lista.append(1213)
# print(numeros_lista)
# numeros_tupla = tuple(numeros_lista)
# print(numeros_tupla)

# datos = [1,2,3,4]
# print(tuple(datos))

# DESAFÍO DE TUPLAS

# tupla = (8,15,4,39,5,89,87,119,7,-755,88,123,2,111,15,9,355)

# tupla_ultimo = tupla[-1]
# tupla_len = len(tupla)
# tupla_busca = tupla.index(87)
# tupla_tres = tupla[-3:]
# tupla_pos = tupla[8]
# tupla_siete = tupla.count(7)

# print(tupla_ultimo)
# print(tupla_len)
# print(tupla_busca)
# print(tupla_tres)
# print(tupla_pos)
# print(tupla_siete)

# 1-EXTRA
# c = "Hola"
# print(c[-1])
# e=(1,2,3)
# print(e[1])
# print(e+(7,8,9))

# 2-EXTRA
# numero_1 = 9
# numero_2 = 3
# numero_3 = 6
# media = (numero_1 + numero_2 + numero_3) /3
# print(media)

# 3-EXTRA
# nota_1 = 10
# nota_2 = 7
# nota_3 = 4

# promedio = nota_1*0.15 + nota_2*0.35+nota_3*0.50
# print(promedio)

# 4-EXTRA
# lista = (1,2,3)
# print(sum(lista))

# mi_tupla[2].append(5)
matriz = [
    [1,5,1],
    [2,1,2],
    [3,0,1],
    [1,4,4]
]

# suma_matriz = sum(matriz[0])
matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))

print(matriz)