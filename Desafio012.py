print(f"{'*'*10}Desafio 012 - Mostra o desconto de um determinado produto{'*'*10}")
valor = float(input("Informe o valor do produto: "))
desconto = int(input ("Informe o desconto a ser dado: "))
print (f"O produto de R${valor} com o desconto de {desconto}% passou a custar: {(valor)*((100-desconto)/100)}")