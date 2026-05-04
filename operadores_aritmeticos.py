#operadores aritmeticos : nos permiten realizar operaciones matematicas


import math
import random

a = 5
b = 10

suma = a + b
print(f"la suma de {a} + {b} es: {suma}")
resta = a - b
print(f"la resta de {a} - {b} es: {resta}")
multiplicacion = a * b
print(f"la multiplicacion de {a} * {b} es: {multiplicacion}")

#division: el resultado de la division siempre es un numero decimal (float)
division = a / b
print(f"la division de {a} / {b} es: {division}")

#division entera: el resultado de la division entera es un numero entero (int) y se redondea hacia abajo
division = a // b
print(f"la division de {a} // {b} es: {division}")

modulo = a % b
print(f"el modulo de {a} % {b} es: {modulo}")

exponente = a**b
print(f"el exponente de {a} ** {b} es: {exponente}")


#precedncia de operadores 

resultado = a + b * 2
print(f"el resultado de la suma de {a} + {b} * {2} es:{resultado}")

resultado2 = (a + b) * 2
print(f"el resultado de la opreacion de {a} + {b} * {2}: {resultado2}")

resultado3 = a * b // 3 
print(f"el resultado de la operacion de {a} * {b} // {3}: {resultado3}")

resultado4 = (a + b) // 3
print(f"el resultado de la operacion de {a} * {b} // {3}: {resultado4}")


ejercicio = ((a+b) * (a - b) / (a * b)) - ((a ** b) % 3)
# ejercicio = ((3+2) * (3-2) / (3*2) - ((3**2) % 3)
# ejercicio = (5 * 1 / 6) - (9 % 3)
# ejercicio = (5 / 6) - 0
#ejercicio = 0.83333333334

print(f"la suma de la operacion ({a} + {b}) * ({a} - {b}) / ({a} * {b}):es{ejercicio}")

#numero pi
print(math.pi)

#numero aleatorio entre 0 y 10
print(random.random())
numero_aleatorio = random.randint(1, 10) # numero aleatorio entre 1 y 10

