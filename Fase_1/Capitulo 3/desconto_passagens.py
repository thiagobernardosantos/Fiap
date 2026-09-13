preco = float(input("Digite o preço bruto da passagem: R$ "))
classe = input("Digite a classe (economica, executiva ou primeira): ").lower()
viajantes = int(input("Digite a quantidade de viajantes: "))

if classe == "economica":
    if viajantes == 2:
        desconto = 3
    elif viajantes == 3:
        desconto = 4
    elif viajantes >= 4:
        desconto = 5
    else:
        desconto = 0

elif classe == "executiva":
    if viajantes == 2:
        desconto = 5
    elif viajantes == 3:
        desconto = 7
    elif viajantes >= 4:
        desconto = 8
    else:
        desconto = 0

elif classe == "primeira":
    if viajantes == 2:
        desconto = 10
    elif viajantes == 3:
        desconto = 15
    elif viajantes >= 4:
        desconto = 20
    else:
        desconto = 0

else:
    desconto = 0
    print("Classe inválida.")

valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

print("Desconto:", desconto, "%")
print("Valor do desconto: R$", valor_desconto)
print("Preço final: R$", preco_final)
