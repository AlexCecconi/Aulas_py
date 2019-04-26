def receber_idade():
		idade = input('Digite sua idade: ')
		idade = int(idade)
		if idade<=0:
			raise Exception('idade menor que zero')
		return idade

def imprimir_idade(idade):
	print ('Voce disse que tem {} anos.'.format(idade))	
	