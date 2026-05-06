# Dados a la suerte
import random

print("BIENVENIDOS AL JUEGOS DE LOS DADOS Y LA SUERTE 🎲")

print("-" * 60)

nombre = input("Hola, como te llamas?: ")

print("-" * 60)

# el usuario escoge un numero y si es igual al de la computadora gana es pura suerte

dado = int(input("Ingresa un numero🎲: "))
resultado_del_dado = random.randint(1, 6)

print("Resultado de la computadora🎲: ", resultado_del_dado)



if resultado_del_dado == dado:
    print("Ganaste")
else:
    print("Perdiste")

print("Quieres perdero ganar de nuevo?😂")







    



