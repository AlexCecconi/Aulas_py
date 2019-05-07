














exit()
# ex2
idade = input('Digite sua idade: ')
letras = '1234567890'
string = ''

for ler in idade:
	if  ler in letras: 
		string += ler
print(string)

exit()
# ex1
idade = input('Digite sua idade: ')
letras = '1234567890'

for ler in idade:
	if ler not in letras: 
		print('Jumento')
		exit()
	else:
		print('boa')
		exit()


