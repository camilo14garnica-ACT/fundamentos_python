#TUPLAS

# Estructura  deun atupla

#Indice      0             1            2
tupla = ("elemeto 1", "elemeto 2", "elemto 3")
print(type(tupla)) # clase tuple

tupla2 = "a", "b", "c"
print(type(tupla2)) # sirve sin corchetes.

tuple_3 = ("hola",) # con la coma se puede convertie en tuple
print(type(tuple_3))

tuple_4 = tuple("hola")
print(tuple_4) # de esta forma se divide la elemento en partes.

tuplas_mixtas = ("hola", 123, 4.14, True, [1, 2, 3])
print(type(tuplas_mixtas)) 

# TUPLA APRENDICES ADSO

#INDICE          0        1         2         3         4
aprendices = ("Simon", "Camilo", "David", "Miguel", "Sharyt")

#acceder aun elelemento de la lista 
print(aprendices[1]) #Camilo
print(aprendices[0:3]) #Simon, Camilo, David

#sumar 2 tuplas
tupla_1 = (1,2,2)
tupla_2 = (4,5,6)
suma_tupla = tupla_1 + tupla_2
print(suma_tupla)

#multiplicar una tupla

tupla_multiplicada = tupla_2 * 3
print(tupla_multiplicada)

#METODOS DE LAS TUPLAS

#medir el largo con len()
print(len(aprendices))

#contar elementos repetidos de una lista
print(aprendices.count("Camilo")) #1

#Obtener el index de un elemento
print(aprendices.index("Simon")) #0

print(type(aprendices))

#MODIFICAR UNA TUPLA A UNA LISTA
aprendices_lista = list(aprendices)
print(type(aprendices_lista))
print("-" * 60)

aprendices_lista.append("Felipe")
print(aprendices_lista)

#MODIFICAR LA LISTA OTRA VEZ A TUPLE
aprendices = tuple(aprendices_lista)
print(type(aprendices))


#COMPROBAR PERTENENCIA (in)
print("Simon" in aprendices) #true
print("Andres" in aprendices) #false

#empaquetar tuplas

programa_1 = "ADSO"
programa_2 = "SST"
programa_3 = "Topografia" 

tupla_programas = (programa_1, programa_2, programa_3)
print(tupla_programas) 

#Desempacar tuplas
tupla_desempaquetada = ("ADSO", "SST", "Topografia")
programa_1, programa_2, programa_3 = tupla_desempaquetada
print(programa_1)

#ejercicio 2

tupla_ciudades = ("bogota", "medellin", "pereira")
ciudad_1, ciudad_2, ciudad_3 = tupla_ciudades
print(ciudad_1)

#iterar sobre una tupla con un ciclo for
for ciudad in tupla_ciudades:
    print(ciudad)
    

print(ciudad)

