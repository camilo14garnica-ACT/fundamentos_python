# Clasificador de IMC


peso = float(input("Ingrese su peso: "))
estatura = float(input("Ingrese su estatura en metros: "))

IMC = peso / (estatura ** 2)

# usar condicionales

if IMC < 18.5:
    print("Bajo peso", round (IMC))
elif IMC >= 18.5 and  IMC <= 24.9:
    print("normal", round(IMC))
elif IMC >= 25 and IMC <= 29.9:
    print("Sobrepeso", round(IMC))
elif IMC >= 30:
    print("Obeso", round(IMC))


