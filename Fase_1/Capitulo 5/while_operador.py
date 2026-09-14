resp = input("Digite [S]im ou [N]ão: ")
while resp not in (‘S’, ‘N’):
    print("Opção inválida! Digite [S]im ou [N]ão.")
    resp = input()
print("Você digitou a letra válida", resp)
