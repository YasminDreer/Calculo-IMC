peso = float(input("Introduza o seu peso (kg): "))
altura = float(input("Introduza a sua altura (cm): "))

altura_m = altura / 100
imc = peso / (altura_m * altura_m)

print(f"\nIMC: {imc:.2f}")

if imc < 18.5:
    print("Fora do peso normal")
elif imc < 25:
    print("Peso normal")
else:
    print("Fora do peso normal")