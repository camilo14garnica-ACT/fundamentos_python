# Condicional if/elif/else

if True:
    print("la primera condicion es verdadera")
elif False:
    print("la segunda conidicion es verdadera")
elif True:
    print("la tercera condicion es falsa")
else:
    print("la condicion es falsa")


# Ejercicio: Clasificacion de edad


edad = int(input("ingresa tu viejura"))

if edad < 18:
    if edad >= 12 and edad < 18:
        print("Lo que tienes es calcio colageno pa gastar")
    else:
        print("Eres un bebe todavia")
else:
    if edad >= 20:
        print("estas apenas mami")
    if edad >= 50:
        print("Ya estas viejo")
        
    

# Operador Terniario
numero = 7

if numero % 2 == 0:
    print("El numero es par")
else:
    print("el numero es impar")