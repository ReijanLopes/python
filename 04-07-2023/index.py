kilometros = float(input("Quantidade de kilometros rodados?"))
Dias = int(input("Quantos dia de uso?"))

valorTotal = Dias * 60 + 0.15 * kilometros

print("km = {}, dias = {}. Valor a se pago = {}".format(kilometros, Dias, valorTotal))