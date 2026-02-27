print("##########################")
print("       calculadora        ")
print("##########################")

import math

print("Tecle a opção desejada e aperte ENTER")
print("1 - SOMA")
print("2 - SUBTRACAO")
print("3 - MULTIPLICACAO")
print("4 - DIVISAO")
print("5 - POTENCIAÇAO")
print("6 - RAIZ QUADRADA")

op = input ("Opção desejada ENTER")
op = int(op)
if (op>6 or op<1):
	print("Opção Inválida!")
	input()
	exit()


if (op == 6):
	a = input("Entre com valor A: ")
	a = int(a)
else:
	a = input("Entre com valor de A: ")
	a = int(a)
	b = input("Entre com valor de B: ")
	b = int(b)


if ( op== 1):
	print("A soma é: ", a+b)
elif ( op== 2):
	print("A subtração é: ", a-b)
elif ( op== 3):
	print("A é multiplicador: ", a*b)
elif ( op== 4):
	print("A divisão é: ", a/b)
elif ( op== 5):
	print("A potenciação é: ", a**b)
elif ( op== 6):
	print("A raiz quadrada é:", math.sqrt(a))

input()