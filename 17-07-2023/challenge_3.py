# Enunciado: Você foi contratado para desenvolver um sistema de cobrança de banho para um petshop. Você ficou com a parte de desenvolver a interface com o funcionário.
# O petshop opera da seguinte maneira:
# Para cães com peso menor que 3 kg o valor base é de 40 reais;
# Para cães com peso igual ou maior que 3 kg e menor que 10 kg o valor base é de 50 reais;
# Para cães com peso igual ou maior que 10 kg e menor que 30kg o valor base é de 60 reais;  
# Para cães com peso igual ou maior que 30 kg e menor que 50kg o valor base é de 70 reais; 

# Para cães com pelo curto (c) o multiplicador é 1;
# Para cães com pelo médio (m) o multiplicador é 1.5;
# Para cães com pelo longo (l) o multiplicador é 2;

# Para o adicional de cortar unhas (1) do cachorro é cobrado um valor extra de 10 reais;
# Para o adicional de escovar os dentes (2) do cachorro é cobrado um valor extra de 12 reais;
# Para o adicional de limpar as orelhas (3) do cachorro é cobrado um valor extra de 15 reais;
# Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;


# O valor final da conta é calculado da seguinte maneira:

#tabelas de valores
tableByWeight = {
    0: 40,
    1: 50,
    2: 60,
    3: 70
}
tableByCoat = {
    "c": 1,
    "m": 1.5,
    "l": 2
}
tableAdditional = {
    1: 10,
    2: 12,
    3: 15,
}

#funções
def cachorro_peso():
    while True:  
        inputWeight = input("Entre com o peso do cachorro: ")

        if inputWeight.isdigit():
            weight = float(inputWeight)
            if weight < 3:
                return 40
            elif weight < 10:
                return 50
            elif weight < 30:
                return 60

            return 70
        else:
            print("Você digitou um valor não numérico")
            print("Por favor entre com o peso do cachorro novamente.")

def cachorro_pelo():
    while True: 
        print("Entre com o pelo do cachorro")
        print("c - Pelo curto")
        print("m - Pelo Médio")
        print("l - Pelo Longo")
        coatType = input(">> ")

        if coatType in ["c", "m", "l"]:
            return tableByCoat[coatType]
        else:
            print("Você digitou um valor inválido")

def cachorro_extra():
    additional = 0
    while True:
        print("Deseja adicionar mais algum serviço")
        print("1 - Corte de Unhas - R$ 10,00")
        print("2 - Escovar Dentes - R$ 12,00")
        print("3 - Limpeza de Orelhas - R$ 15,00")
        print("0 - Não desejo mais nada")
        try:
            extra = int(input(">> "))
            if extra == 0: break
            if extra not in [1, 2, 3]:
                raise ValueError
            else:
                additional += tableAdditional[extra]
        except ValueError:
            print("Tamanho de pelo inválido.")
    
    return additional

#resultado
Weight = cachorro_peso()
coat = cachorro_pelo()
extra = cachorro_extra()

total = Weight * coat + extra
# formatando para que fique igual ao exemplo
totalFormat = f"{total:.2f}"
print("Total a pagar(R$): {} (peso: {} * pelo: {} + adicional(is): {})".format(totalFormat, Weight, coat, extra))