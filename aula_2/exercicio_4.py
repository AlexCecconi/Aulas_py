somar = 0
contar = 0

arquivo = open('argumentos.txt','r');
for i in arquivo.readlines():
	somar = somar + int(i)
	contar += 1	
dividir=somar/contar
print(dividir)












