def double_input():
    lista = []
    while True:
    	num = float(input("Digite um número:"))
    	if (num > 0):
    		lista.append(num*2)
    	else:
    		break
    print (lista)


double_input()