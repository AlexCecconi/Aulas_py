def tratar_excecao(fn):
	def wrapper(*args, **kwargs):
		try:
			return fn(*args, **kwargs)
		except:
			print('Opa....deu ruim')
		return wrapper	


exit()
#funcao retorna funcao
def funcao_que_retorna_funcao():
	def f():
		return 10
	return f 

funcao = funcao_que_retorna_funcao()
valor = funcao()
print()





