#Crea actividad2_listas.py con la siguiente lista de temperaturas registradas durante, dos semanas
temperaturas = [18, 21, 19, 24, 22, 20  ,17, 23, 25, 21, 18, 20, 22, 19]
print("--" * 50)

#Usa indexación para imprimir la temperatura del primer día, el último día, el día 7, (mitad) y el penúltimo día, usando tanto índices positivos como negativos.
print(f"la temperatura del dia 1 es {temperaturas[0]}")
print(f"la temperatura del 11 es {temperaturas[-3]}")
print(f"la temperatura del dia 7 es {temperaturas[6]}")
print(f"la temperatura del penultimo dia es {temperaturas[12]}")
print("--" * 50)

# slicing para extraer e imprimir: la primera semana (días 1–7), la segunda, semana (días 8–14)

print(f"las temperaturas de la primera semana son {temperaturas[0:7]}")
print(f"las temperaturas de la segunda semana son {temperaturas[7:14]}")
print("--" * 50)

# Solo los días pares de toda la quincena (días 2,4,6,8,10,12,14)
print(f"las temperaturas de los días pares son {temperaturas[1::2]}")
print("--" * 50)

# La lista de temperaturas en orden invertido
print(f"las temperaturas en orden invertido son {temperaturas[::-1]}")
print("--" * 50)

#Calcula e imprime la temperatura promedio de cada semana por separado usando, sum() y len() aplicados a los slices.

primera_semana_1 = temperaturas[0:7]
segunda_semana_2 = temperaturas[7:14]

promedio_semana_1 = sum(primera_semana_1) / len(primera_semana_1)
promedio_semana_2 = sum(segunda_semana_2) / len(segunda_semana_2)

print(f"el promedio de la semana 1 es {int(promedio_semana_1)}")
print(f"el promedio de la segunda semana es {int(promedio_semana_2)}")
print("--" * 50)

#BONUS Determina cuál de las dos semanas tuvo mayor temperatura promedio

if promedio_semana_1 > promedio_semana_2:
    print("la semana uno tuvo mayor promedio")
elif promedio_semana_1 < promedio_semana_2:
    print("la segunda semana tuvo mayor promedio")
else:
    ("la semanas tuvieron el mismno promedio")

print("--" * 50)
