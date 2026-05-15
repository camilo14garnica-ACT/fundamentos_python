#CONJUNTOS SET CON PHYTON 

# ---creacion---

lenguajes = { "phyton", "java", "c++", "phyton", "java"}
print(lenguajes)  #no deja duplicados

# metodos de modificacion.

frutas = {"manzana", "guayaba", "pera"}
frutas.add("maracuya")
frutas.add("mango")
frutas.add("uva")
frutas.add("banano")
frutas.add("manzana") # no se repite no admite duplicidad
print(frutas)
elem = frutas.pop() #eescoge y elimina un elemento al azar y se gaurda en la variable elem
print(elem)

python_devs = {"Ana", "luisa", "sharyt", "camilo", "david", "miguel"}
java_devs = {"luisa", "Diego", "sofia", "david", "andrea", "Ana"}

#UNION
#para unir los 2 conjuntos
union = python_devs.union(java_devs)
print(union)
#lo mismo pero de otra manera
todos = python_devs | java_devs
print(todos)

#INTERSECCION
ambos = python_devs & java_devs
print(ambos)
#otra manera 
interseccion = python_devs.intersection(java_devs)
print(interseccion)


#DIFERENCIA -
solo_python = python_devs - java_devs
print(solo_python)
#otra manera
diferencia = python_devs.difference(java_devs)
print("solo python:", diferencia)

solo_jaava = java_devs - python_devs
print(solo_jaava)

#DIFERENCIA SIMETRICA
exclusivos = python_devs ^ java_devs
print(exclusivos)
#otra manera 
diferencia_asimetrica = python_devs.symmetric_difference(java_devs)
print(diferencia_asimetrica)

