def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    else:
        return "Obesidade"


imcs = []
classificacoes = []

while True:
    try:
        peso = float(input("Introduza o seu peso (kg): "))
        altura = float(input("Introduza a sua altura (cm): "))

        if peso <= 0 or altura <= 0:
            print("Valores têm de ser maiores que zero.")
            continue

        imc = peso / (altura / 100) ** 2
        classificacao = classificar_imc(imc)

        print(f"\nIMC: {imc:.2f}")
        print(f"Classificação: {classificacao}\n")

        imcs.append(imc)
        classificacoes.append(classificacao)

    except ValueError:
        print("Valor inválido! Introduza um número.")
        continue

    resposta = input("Deseja continuar? (s/n): ").strip().lower()
    if resposta in ("n", "não", "nao"):
        break

print("\n--- Resumo ---")
print(f"Total de consultas: {len(imcs)}")
print(f"Média do IMC: {sum(imcs) / len(imcs):.2f}")
print(f"Classificação mais frequente: {max(set(classificacoes), key=classificacoes.count)}")