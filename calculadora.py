# calculadora.py

# Calculadora básica en Python

valor_1 = float(input("Ingrese el primer valor:"))
valor_2 = float(input("Ingrese un segundo valor: "))
tipo_de_operacion = int(input("Ingrese el tipo de operacion que desea realizar (1. Suma, 2. Resta, 3.Multiplicacion, 4.Division, 5.potensiacion)"))

# Realizar la operacion dependiendo el numero escogido

suma = valor_1 + valor_2
resta = valor_1 - valor_2
multiplicasion = valor_1 * valor_2
division = valor_1 / valor_2
potenciacion = valor_1 ** valor_2


if tipo_de_operacion == 1:
    suma = valor_1 + valor_2
    print(f"la suma entre {valor_1} y {valor_2} es: {suma}")
elif tipo_de_operacion == 2:
    resta = valor_1 - valor_2
    print(f"la resta entre {valor_1} y {valor_2} es {resta}")
elif tipo_de_operacion == 3:
    multiplicacion = valor_1 * valor_2
    print(f"la multiplicasion entre {valor_1} y {valor_2} es {multiplicasion}")
elif tipo_de_operacion == 4:
    division = valor_1 / valor_2
    print(f"la division entre {valor_1} y {valor_2} es {division}")
elif tipo_de_operacion == 5:
    poteniacion = valor_1 ** valor_2
    print(f"la potensiacion entre {valor_1} y {valor_2} es {potenciacion}")
else:
    print("operacion no valida")