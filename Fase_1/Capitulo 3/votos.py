playstation = 0
xbox = 0
nintendo = 0

for i in range(5):
    voto = input("Digite sua preferência (playstation, xbox ou nintendo): ").lower()

    if voto == "playstation":
        playstation += 1

    elif voto == "xbox":
        xbox += 1

    elif voto == "nintendo":
        nintendo += 1

    else:
        print("Opção inválida!")

print("\nResultado da votação:")
print("PlayStation:", playstation, "votos")
print("Xbox:", xbox, "votos")
print("Nintendo:", nintendo, "votos")

if playstation > xbox and playstation > nintendo:
    print("Os usuários ganharam um PlayStation!")

elif xbox > playstation and xbox > nintendo:
    print("Os usuários ganharam um Xbox!")

elif nintendo > playstation and nintendo > xbox:
    print("Os usuários ganharam um Nintendo!")

else:
    print("Houve empate!")
