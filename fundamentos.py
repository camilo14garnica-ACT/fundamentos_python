from math import e


print("HELLO WORLD")

mi_variable = "Hola Mundo" 
print(mi_variable)


calCase = "SENAA"
PascalCase = "SENA"
Snake_case = "SENA" #usaremos este estilo de nombres para variables

print("snake_case")


x = "esta es una x minuscula"
x = "otro valos distinto a x" 

print(x)

print(type(2))
print(type(3.5))
print(type(True))
print(type('hola'))
print(type(1+3j))

#variables con diferentes tipos de datos

nombre = "camilo"
apellido = "Orduz"
edad = 20
altura= 1.75
activo = True
correo = " camilo1.0garnica@gmail.com"
telefono = "3224113371"

#type: nos permite conocer el tipo de dato de una variable

print(type(nombre))
print(type(apellido))
print(type(edad))
print(type(altura))
print(type(activo))
print(type(correo))
print(type(telefono))


#casting: convertir un tipo de dato a otro tipo de dato

telefono_int = int(telefono)
print(type(telefono_int))
print(type(telefono_int), telefono_int)

edad_float = float(edad)
print(type(edad_float))
print(type(edad_float), edad_float)

altura_int = int(altura)
print(type(altura_int))
print(type(altura_int), altura_int)

"""
__Nota: El casting puede generar errores si el valor no es compatible con el tipo de dato al que se quiere convertir. 
Por ejemplo, si intentamos convertir una cadena de texto que no representa un número a un entero, se generará un error.
    
"""

#identacion en python 
if 5 > 2:
    print("5 es mayor que 2")
else:
    print("5 no es mayor que 2")

#input: nos permite solicitar al usuario que ingrese un valor por teclado

nombre_completo = input ("Ingrese su nombre completo:")
print("hola", nombre_completo)


edad = int(input("Ingrese su edad"))
print(type(edad), edad)


#f-string: nos permite imprimir cadenas de texto de manera más sencilla y legible
print(f"hola{nombre_completo}, tu edad es {edad}, años")


