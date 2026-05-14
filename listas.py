# listas 

# estrutura de lista 

# indice : 0     1      2    3    4   5

# indice negativos: -4    -3     -2   -1

listas = ["objeto_1, objeto_2, objeto_3,"]

print(type(listas))    # <class 'list'>

listas_mixtas = ["si o que marino", 25, 3.14, True]

# LISTA DE APRENDICES

aprendices = ["pablo ", "lian", "emirio", "pedro", "luis"]
print(aprendices)


# acceder a un elemento de la lista

print(aprendices[2]) # emirio

# modificar la lista

aprendices[1] = "camila"
print(aprendices)

# consultar rangos de la lista

print(aprendices[1:4]) # camila, maria, pedro
print(aprendices[2:3])  # emirio
print(aprendices[:3]) # pablo, camila, emirio
print(aprendices[0 :: 2]) # pablo, emirio, luis



# unir 2 listas

aprendices_ficha_3321349 = ["Jhon", "Mario", "Mario", "Andres"]
aprendices_ficha_2321322 = ["Maria", "Luna", "Miguel"]

Aprendices_unidos = aprendices_ficha_2321322 + aprendices_ficha_3321349
print(Aprendices_unidos)


# medir el largo con len() para saber cuantos hay en la lista.
print(len(Aprendices_unidos))

#contar elementos repetidos
count_Mario = aprendices_ficha_3321349.count("Mario")
print(f"el aprendiz aparece {count_Mario} veces en la lista")

print(aprendices_ficha_3321349.count("Sofia"))

# obtener el indice de un elemento con index

indice_Jhon = aprendices_ficha_3321349.index("Jhon")
print(f"el indice de Jhon es {indice_Jhon}")
