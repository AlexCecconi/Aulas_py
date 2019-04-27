#calcula a area de um quadrado, e o volume do cube

def calcula_area(a,b):
	return a*b

def calcula_cubo(a,b,c):
	return c*calcula_area(a,b)

calculacubo = calcula_cubo(2,2,2)
print(calculacubo)


exit()
def soma(a,b):
	return a+b

lista_de_numeros = [1,2,3,4,5,6,7]
def somar_lista_de_numeros():
	resultado_da_soma = 0
	for numero in lista_de_numeros:
		resultado_da_soma = soma(resultado_da_soma+numero)
	return resultado_da_soma	

SomaLista = somar_lista_de_numeros()	
print(SomaLista)


exit()
#exercicio 2
#escrever uma funcao que recebe dois numeros e retorna o maior deles
def escolhe_max(a,b):
	if a<b:
		return b
	else:
		return a

EscolheMax = escolhe_max(7,3)
print(EscolheMax)


exit()
def nome_da_funcao():
	return  'valor retorno'

	#exerccio 0
	#funcao q soma dois numeros
def soma(a,b):
	return a+b

#Exercicio1
#escrever uma funcao que retorna a soma de uma lista de numeros

lista_de_numeros = [1,2,3,4,5,6,7]
def somar_lista_de_numeros():
	resultado_da_soma = 0
	for numero in lista_de_numeros:
		resultado_da_soma += numero
	return resultado_da_soma	
Valor_de_retorno = nome_da_funcao()