#operadores aritmeticos : nos permiten realizar operaciones matematicas

from pickletools import int4


a = float( input("Ingrese el primer número: "))
b = float( input("Ingrese el segundo número: "))
tipo_de_operacion = input("Ingrese la operacion que desea realizar: 1.suma, 2.resta, 3.multiplicacion, 4.division, 5.modulo, 6.potencia:")


suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
potencia = a ** b
print("suma", suma)

if tipo_de_operacion == "1":
    print("suma", suma)
elif tipo_de_operacion == "2":
    print("resta", resta)
elif tipo_de_operacion == "3":
    print("multiplicacion", multiplicacion)
elif tipo_de_operacion == "4":
    print("division", division)
elif tipo_de_operacion == "5":
    print("modulo", modulo) 
elif tipo_de_operacion == "6":
    print("potencia", potencia)

   


