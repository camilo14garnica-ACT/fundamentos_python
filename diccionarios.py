# DICCIONARIOS (caracteristicas a un elemento)

#creacion de un diccionario

# estructura de un diccionaio

diccionario = {
    "clave_1" : "valor_1",
    "clave_2" : "valor_2",
    "clave_3" : "valr_3" 
}

# diccionario vaio
diccionario_vacio = {}

#Diccionario con elementos

diccionario_aprendiz = {
    "nombre" : "Camilo",
    "apellido" : "Garnica",
    "programa" : "ADSO",
    "edad" : 20
}
print(type(diccionario_aprendiz))


#obtener un valor del diccionario.
print(diccionario_aprendiz["programa"])
print(diccionario_aprendiz["nombre"])
print(diccionario_aprendiz["apellido"])
print(diccionario_aprendiz["edad"])


#obtener solo las claves del Diccionario
print(diccionario_aprendiz.keys()) #['nombre', 'apellido', 'programa', 'edad']

#Obtener solo los valores del Diccionario
print(diccionario_aprendiz.values()) # "camilo", "garnica", "ADSO", "20"

#Agregar un nuevo elemento al Diccionario
diccionario_aprendiz["correo"] = "camilo1.0garnica@gmail.com"
print(diccionario_aprendiz)

#Modificar un elemento de la tabla
diccionario_aprendiz["programa"] = "Aguas residuales"
print(diccionario_aprendiz)


#Metodo UPDATE
diccionario_aprendiz.update({"nombre" : "Brayan"})
diccionario_aprendiz.update({"apellido" : "Orduz"})
print(diccionario_aprendiz)


#comprobar pertenencia 
if "nombre" in diccionario_aprendiz:
    print("Nombre es una de las propiedades de este diccionario")


#Recorrer solo las claves del Diccionario
for i in diccionario_aprendiz.keys():
    print(i) #osea se imprime cada eñlemento en una limnea aparte
    
    
#obtener las claves y valores de un diccionario.
for clave, valor, in diccionario_aprendiz.items():
    print(f"{clave} :{valor}")
    

#Eliminar elementos de un diccionario con POP()
diccionario_aprendiz.popitem() #elimina el ultimo elemento del diccionario
print(diccionario_aprendiz)

diccionario_aprendiz.pop("edad") #eliminar un elemento en especifico
print(diccionario_aprendiz)

#eliminar todos los elementos de un programa
diccionario_aprendiz.clear()
print(diccionario_aprendiz)


# DICCIONARIOS ANIDADOS

aprendices = {
    "aprendiz_1":{
        "nombre" : "Camilo",
        "apellido" : "Garnica",
        "programa" : "ADSO",
        "edad" : 20
    },
    "aprendiz_2" : {
        "nombre" : "sharyt",
        "apllido" : "medina",
        "programa" : "ADSO",
        "edad" : 18
    },
    "aprendiz_3" : {
        "nombre": "david",
        "apellido" : "lopez",
        "programa" : "ADSO",
        "edad" : 19
        }
}
print(aprendices)

# Acceder aun elemeneto del diccionario
print(aprendices["aprendiz_1"]["nombre"])
print(aprendices["aprendiz_3"]["programa"])

#Recorrer un diccionar anidado con el ciclo FOR.
for aprendiz, datos in aprendices.items():
    print(f"{aprendiz}")
    for clave, valor in datos.items():
        print(f"{clave}, {valor}")
        


