for x in range(1):
	print("Ola mundo")


a = int(input("Digite um número: "))
div = 0

for x in range(1, a+1):
	resto = a % x
	if resto == 0:
		div += 1
if div == 2:
	print("O número é primo !!")
else:
	print("O número não é primo")