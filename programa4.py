# # # # # # # # # # # # # # # # #
# # CONTROLADORES DE FLUJO # # # #

# forma de entender la sucesión
# de las instrucciones de un programa

#       IF

# edad = int(input("Ingrese su edad: "))
# if edad >=18:
#     print("Es adulto")

# a=25
# b=50
# if b>a:
#     print("b es más que a")

# a=195
# b=30
# c=400
# # and
# if a>b and c>a:
#     print("ambas condiciones son verdaderas")

# # or
# if a>b or a>c:
#     print("al menos una condición es verdadera")

# # not
# x = 10
# if not x>15:
#     print("False")

# una sola línea
# a=150
# b=35
# if a>b:print("a es mayor que b")

# if y else también en una sola línea
# a=5
# b=150
# print("A") if a>b else print("B")

#   ELSE
# numero = 24
# if numero >35:
#     print("el número es grande")
# else:
#     print("numero es menor que 35")

#   MULTIPLES IF
# x=19
# if x>10:
#     print("X es más que 10")
#     if x>20:
#         print("X también es más que 20!")
#     else:
#         print("pero no que 20")
        
#   ELIF
# a = 2+3
# if a==4:
#     print("A es igual a cuatro")
# elif a==5:
#     print("A es igual a cinco")
# elif a==6:
#     print("A es igual a seis")
# else:
#     print("A no cumple la condición")
    
#       1-DESAFÍO
# año_nacimiento = int(input("Ingrese su año de nacimiento: "))

# if 1920 <= año_nacimiento <= 1940:
#     print("Pertenece a la generación silenciosa")
# elif 1946 <= año_nacimiento <= 1964:
#     print("Pertenece a la generación Baby Boomer")
# elif 1965 <= año_nacimiento <= 1979:
#     print("Pertenece a Generación X")
# elif 1980 <= año_nacimiento <= 2000:
#     print("Pertenece a Generación Y")
# elif 2001 <= año_nacimiento <= 2010:
#     print("Pertenece a Generación Z")
# else:
#     print("No existe generación asociada")

#       2-DESAFÍO
edad = int(input("Ingrese su edad: "))
antiguedad = int(input("Años de ser cliente: "))
ingreso = int(input("Cuál es su ingreso mensual?: "))

# if edad>=18 and antiguedad>=3 and ingreso>=2500:
#     print("Credito aprobado!")
if edad>=18:
    if antiguedad>=3:
        if ingreso>=2500:
            print("Credito aprobado!")
        else:print("No tiene ingresos suficientes")
    else:
        if ingreso>=4000:
            print("Credito aprobado!")
        else:
            print("No tiene antigüedad suficiente")
else:
    print("No alcanza la edad suficiente")