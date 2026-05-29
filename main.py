peso = float(input("Introduza o seu peso (kg): "))
altura = float(input("Introduza a sua altura (cm): "))

altura_m = altura / 100
imc = peso / (altura_m * altura_m)

print(f"\nIMC: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <25:
    print("Peso normal")
elif imc >= 25 and imc < 30:
    print("Excesso de Peso")
elif imc >= 30:
    print("Obesidade")