# SENTENCIAS ITERATIVAS
# controlar el flujo

# Flujo: sucesión de instrucciones de un programa
# se ejecutan una desepués de otras de manera ordenada

# ITERAR
# 1-WHILE
#       evalúa si es True o False
#       Si False sale de la sentencia While y continúa con la siguiente ejecución
#       Si True ejecuta c/u de las sentencias en el bloque de código

# BUCLE
#       vuelve arriba
#       si False a la primera vez que se pasa el bucle, las sentencias del interior
#       del bucle NO SE EJECUTAN nunca

# num = 5
# while num>0:
#     print(f'{num}')
#     num-=1
# print("terminó el conteo!")

# 2-WHILE-ELSE
#       ejecutar bloque de código cuando bucle while tenga condición False
#       o haya terminado y no haya sido forzado a salir mediante un break

# chance =1
# while chance<=3:
#     txt =input("Escribe SI:")
#     if txt == "SI":
#         print("Ok, lo conseguiste en el intento",chance)
#         chance=10   #el 10 es para cortar, transformándolo en False y saliendo
#     chance+=1
# else:
#     print("Has agotado tus 3 intentos")

#      DESAFÍO ! ! !

# num=[]
# while len(num)<3:
#     num.append(int(input("Números a sumar: ")))
#     suma_num = sum(num)


# print("Ingresados: ", num)
# print("Resultado: ", suma_num)

# Inicializar variables

# suma_total = 0
# a=True

# while a:
#     entrada = input("Ingresa un número o escribe 'exit' para salir: ")

#     if entrada == 'exit':
#         a=False

#     else:
#         numero = int(entrada)
#         suma_total += numero
#         print(f"Suma total: {suma_total}")

# print("Programa finalizado. Suma total:", suma_total)

# DESAFÍO #1


# i = 1
# while i<6:
#     print(i)
#     if i==3:
#         break
#     i+=1

#       BREAK

# x = 5
# while True:
#     x-= 1
#     print(x)
#     if x ==0:
#         print("Fin del bucle")
#         break

#       CONTINUE

# i=0
# while i<6:
#     i+=1
#     if i ==3:
#         continue    #acá continúa al resto del código (bucle) por lo que
#     print(i)        # parece saltearlo. Wow!
    
#       PASS
# permite manejar la condición sin que el bucle se vea afectado
# el código se sigue leyendo, salvo BREAK

# n =0
# while n<10:
#     n+=1
#     if n==2:
#         pass
#     print('n vale',n)
    
# m=0
# while m<10:
#     m+=1
#     if m==2:
#         pass
#         print("m vale",m)
        
# c=-3
# while c<10:
#     c+=1
#     if c==2:
#         pass
#     print("c vale", c)


#       FOR
# en cada paso de la iteración se tiene en cuenta a un único elemento
# del objeto iterable, sobre el cual se pueden aplicar operaciones

# lista = [1,2,3,4,5]
# for valor in lista:
#     print("Soy un item de la lista y valgo",valor)
# # se definió como 'valor' a cada item de la lista
# # que solamente vale para el objeto que está iterando

# lista = [0,1,2,3]
# for num in lista:
#     print("Soy un valor de la lista y valgo",num)
#     num*=5
#     print("Soy un valor de la lista y ahora valgo", num)
#     num/=5
#     print("Y ahora vuelvo a valer", num)

# Modificando la lista
# indice=0
# numeros=[6,7,8,9,10,5]
# for numero in numeros:
#     numeros[indice]*=5  
#     indice+=1
# print(numeros)

# Sentencia For

# texto = "Hola mundo, estoy usando Python"
# for letra in texto:
#     print(letra)
# texto2=""
# for letra in texto:
#     texto2=letra*2
# print(texto2)


#       RANGE

# el for necesita colección de datos para poder ser usado,
# en otros lenguajes necesitamos solamente un número para
# indicar las iteraciones a cumplir

# para simularloo está la función range() que representa
# una colección de números inmutables

# Constructores para crear objetos Range

# #   1-  range(fin):
# #       crea una secuencia que va desde 0 hasta fin -1

# for numero in range(10):
#     print(numero)

# #   2- range(inicio, fin):
# #       secuencia numérica que va desde inicio hasta fin -1

# for numero in range(1,5):
#     print(numero)
    
# #   3- range(inicio, fin [paso])

# for numero in range(4,25,2):
#     print(numero)

#       la ventaja con la lista[] es que ocupa menos espacio en memoria
#       lista[] lee todo e imprime, mientras que con range() interpreta
#       inicio-fin y ejecuta. Genera los números sobre la marcha y no
#       acumulando datos, se ejecuta el 0 y se crea, cuando se ejecuta
#       el 1 se crea el 1 y se elimina el 0. Así sucesivamente


#       FOR-ELSE

# for numero in range(10):
#     print("numero vale", numero)
# else:
#     print("se terminó de iterar y el número vale:",numero)
    
#       FOR-BREAK-CONTINUE-PASS

# for numero in range(10):
#     if numero==2:
#         continue
#     elif numero ==8:
#         break
#     else:
#         print("Se terminó de iterar y número vale:", numero)
        
#       ENUMERATE

# frutas =["manzana","pera","sandía"]
# for indice, fruta in enumerate(frutas):
#     print(f"Índice: {indice}, Fruta: {fruta}")

cancion="Me gusta"
cosas = ["aviones","viajar","mañana","viento","soñar","la mar"]
tu=", me gustas tú"

for indice, cosa in enumerate(cosas):
    print(f"{cancion} {cosa} {tu}")