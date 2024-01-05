# # # # # # # # # # # # # # # # # # # # #
# # OPERADORES # # # # # # # # # # # # # # 

# = es asignación
# == es igualdad
# != desigualdad
# > <
# >=
# <=

# a = 1+1 == 2
# print(a)
# b = 4
# consulta = b!=4
# print(consulta)

# se pueden consultar también listas, booleanos y str
# a = "hola"
# print(a[0] != "2")
# print("hola" == "hola")

# expresiones = [
#     False == True,
#     10 == 2*4,
#     33/3 == 11,
#     True>False,
#     True*5 == 2.5*2
# ]

# print(expresiones)



# # # # # # # # #
# NOT | OR | AND

# a = 4 == 2+2
# b = 2 == 1+1

# print("and: ", a and b) # todo debe ser verdad para que sea True
# print("or: ", a or b) # una, otra o ambas verdaderas hace True

# operadores lógicos
# expresiones = [
#     not False,
#     not 3 == 5,
#     33/3 == 11 and 5>2,
#     True or False,
#     True*5 == 2.5*2 or 123>=23,
#     12>7 and True < False
# ]
# print(expresiones)

# EXPRESIONES ANIDADAS

# nombre = input("Ingrese nombre: ")
# edad = int(input("Ingrese edad: "))
# comprobar = nombre != "****" and 8>len(nombre)>=4 and 20>edad>5 and edad*3>35

# print("hola",nombre,"de",edad,"años")
# print("Se cumplen los requisitos? ", comprobar)

# OPERADORES DE ASIGNACIÓN
# necesitan solo una variable numérica

# numero = 15
# print(numero)
# numero+=1
# print(numero)

# podemos hacer un producto a un valor
# a=5
# a*=10
# b=a
# print(b)
