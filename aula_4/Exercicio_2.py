def calcular_media(*args):
	soma, quantidade = 0, 0
	for nota in args:
		soma, quantidade = soma+nota, quantidade+1
	return soma/quantidade if quantidade > 0 else 0

def calcular_nota(**kwargs):
	for key in kwargs.key():
		kwargs[key] = calcular_media(*kwargs[key])
	return

# calcular_nota(lucas=10, alex=5, paulo=2.5, erick=1.25, victor=0.75)

alunos = {
	'lucas' : [10,10,10]
	'alex' : [5,3,20]
}

medias = calcular_nota(**alunos)
print(medias)





exit()
def criar_moto(tempo_do_motor, numero_marchas, *args):
	return {
		'tempo':tempo_do_motor,
		'marcha' : numero_marchas,
		'marcas' : list(args)
	}

criaMoto = criar_moto(2,5,'honda')
print(cria)





exit()
#escreva uma funcao que receba um numero
#variavel de nomes e retorne uma lista
#daqueles q contém L

def NomesL(*args):
	lista_de_nomes = []
	for nome in args:
		if 'l' in nome.lower():
			lista_de_nomes.append(nome)
	return lista_de_nomes		



		# if n in L:
		# 	return n 
extrai_usuario = NomesL('lucas','ale','carreto')
print(extrai_usuario)