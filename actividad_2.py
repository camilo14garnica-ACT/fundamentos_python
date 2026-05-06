nota_1 = float(input("Ingrese la nota 1: "))
nota_2 = float(input("ingrese la nota 2: "))
nota_3 = float(input("Ingrese la nota 3: "))


if nota_1 <= 5 and nota_2 <= 5 and nota_3 <= 5:
    promedio = (nota_1 + nota_2 + nota_3) / 3
else:
    print("las calificaciones no pueden ser mayores que 5")
    exit()

#calcular puntos faltantes para 5.0

NOTA_MAXIMA = 5.0
faltante = 5.0 - promedio

# verificar si aprueba

aprueba = promedio >= 3.0

# Mostrar resultados

print("\n--resultados--")
print("Promedio",  round(promedio, 2))
print("puntos faltantes para 5.0", round(faltante, 2))

if aprueba:
    print("Estado: Aprueba 👌3")
else:
    print("Estado: No aprueba 😭")
    