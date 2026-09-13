assinatura = input("Digite sua assinatura (basic, silver, gold ou platinum): ").lower()
faturamento = float(input("Digite o faturamento anual: R$ "))

if assinatura == "basic":
    porcentagem = 30

elif assinatura == "silver":
    porcentagem = 20

elif assinatura == "gold":
    porcentagem = 10

elif assinatura == "platinum":
    porcentagem = 5

else:
    porcentagem = 0
    print("Assinatura inválida.")

valor = faturamento * porcentagem / 100

print("Valor que o cliente deve pagar: R$", valor)
