# Se quantidade for menor que 200 o desconto será de 0%;
# Se quantidade for igual ou maior que 200 e menor que 1000 o desconto será de 5%;
# Se quantidade for igual ou maior que 1000 e menor que 2000 o desconto será de 10%;
# Se quantidade for igual ou maior que 2000 o desconto será de 15%;

print("Bem-vindo a Loja do Reijan Lopes de Jesus")

productValue = float(input("Entre com o valor do produto:"))
quantity = int(input("Entre com a quantidade do produto:"))

discount = 0
if quantity >= 200:
    discount = 0.05
elif quantity >= 1000:
    discount = 0.1
elif quantity >= 2000:
    discount = 0.15
else:
    discount = 0

total = productValue * quantity
totalWithDiscount = total - (total * discount)

print("O valor SEM desconto: R$ {}".format(total))

# Não vejo a necessidade de adicionar desconto se não houver desconto
if discount != 0:
    print("O valor COM desconto: R$ {}".format(totalWithDiscount))