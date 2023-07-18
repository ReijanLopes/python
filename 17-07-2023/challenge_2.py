# 1 bola de sorvete no sabor tradicional (tr) custa 6 reais, no sabor premium (pr) 7 reais e no especial (es) 8 reais;
# 2 bolas de sorvete no sabor tradicional (tr) custam 11 reais, no sabor premium (pr) 13 reais e no especial (es) 15 reais;
# 3 bolas de sorvete no sabor tradicional (tr) custam 15 reais, no sabor premium (pr) 18 reais e no especial (es) 21 reais;

flavorsOptions = {
    "tr": "TRADICIONAL",
    "pr": "PREMIUM",
    "es": "ESPECIAL"
}

value = {
    "tr": {
        1: 6,
        2: 10,
        3: 14
    },
    "pr":{
        1: 7,
        2: 12,
        3: 17
    },
    "es": {
        1: 8,
        2: 14,
        3: 20
    },
}

print("Bem-vindo a Sorveteria do Reijan Lopes de Jesus")
print("-" * 38 + "Cardápio" + "-" * 37)
print("| N˚ DE BOLAS | Sabor tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |")
print("|      1      |        R$ 6,00         |       R$ 7,00      |        R$ 8,00      |")
print("|      2      |        R$ 10,00        |       R$ 12,00     |        R$ 14,00     |")
print("|      3      |        R$ 14,00        |       R$ 17,00     |        R$ 20,00     |")
print("-" * 83)

flavor = -1
amountOfBalls = -1
total = 0


while True:
    inputFlavor = input("Entre com o sabor desejado (tr/es/pr): ")
    if inputFlavor == "tr" or inputFlavor == "es" or inputFlavor == "pr":
        flavor = inputFlavor
    else: 
        print("Sabor inválido. Tente novamente")
        continue

    inputAmountOfBalls = int(input("Entre com o número de bolas de sorvete desejado (1/2/3): "))
    if inputAmountOfBalls in [1, 2, 3]:
        amountOfBalls = inputAmountOfBalls
    else: 
        print("Número de bolas de sorvete inválido. Tente novamente")
        continue

    singularOrPlural = "bola" if amountOfBalls == 1 else "bolas"
    print("Você pediu {} {} de sorvete no sabor {}: R$ {},00".format(amountOfBalls, singularOrPlural, flavorsOptions[flavor], value[flavor][amountOfBalls]))
    total += value[flavor][amountOfBalls] # eu alterei para a palavra correta
    repeat = input("Deseja mais algum sorvete (s/digite outra tecla): ")
    if repeat != "s": break

# vou adicionar vírgula aqui ao invés de ponto
print("O valor total a ser pago: R$ {},00".format(total))

        
