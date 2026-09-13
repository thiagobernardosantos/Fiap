idade = int(input("Digite sua idade: "))
batimentos = int(input("Digite seus batimentos cardíacos (BPM): "))

if idade <= 2:
    minimo = 120
    maximo = 140

elif idade <= 17:
    minimo = 80
    maximo = 100

elif idade <= 59:
    minimo = 70
    maximo = 80

else:
    minimo = 50
    maximo = 60

if batimentos < minimo:
    print("Os batimentos estão abaixo do esperado.")

elif batimentos > maximo:
    print("Os batimentos estão acima do esperado.")

else:
    print("Os batimentos estão dentro do esperado.")
