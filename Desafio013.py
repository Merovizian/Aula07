print(f"{'*'*10}Desafio 013 - Mostra o reajuste de um salario{'*'*10}")
salario = float(input("Informe o seu salario: "))
reajuste = int(input("Informe o reajuste a ser dado: "))
print (f"O Salario passou de R${salario} para R${salario*((reajuste/100)+1):.2f}")