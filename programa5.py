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

lista = [1,2,3,4,5]
for valor in lista:
    print("Soy un item de la lista y valgo",valor)