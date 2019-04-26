Banco_Dados = []
Banco_Dados.append({
	'email' : 'alex@gmail.com',
	'idade' : 25,
	'senha' : 'admin'
	})

class InvalidEmailError(Exception)
	pass

class InvalidAgeError(Exception)
	pass

class UsuarioJaCadastradoError(Exception)
	pass

def receber_novo_usuario():
	#recebe os dados do novo usuario
	'email' = input('Digite se e-mail: ')
	if '@' not in usuario['email']:
		raise InvalidEmailError

	idade = int(input('Digite sua idade'))
	if usuario['idade'] <0 :
		raise InvalidAgeError

#retorna o usuario criado
	return {
		'email' = email,
		'idade' = idade
		}
def cadastrar_usuario(usuario):
	for cadastrar_usuario in Banco_Dados
		if cadastrar_usuario['email'] == usuario['email']:
			raise UsuarioJaCadastradoError




try:
	usuario = cadastrar_usuario()
	cadastrar_usuario
	print('usuario cadastrado com sucesso')
except InvalidEmailError as err:
	print('erro email')

except InvalidAgeError as err:
	print('erro idade')














exit()
Banco_Dados = []

class InvalidEmailError(Exception)
	pass

class InvalidAgeError(Exception)
	pass

def receber_novo_usuario():
	#recebe os dados do novo usuario
	usuario = {
		'email' : input('Digite se e-mail: '),
		'idade' : int(input('Digite sua idade: '))
	}
	if '@' not in usuario['email']:
		raise InvalidEmailError

	if usuario['idade'] <0 :
		raise InvalidAgeError

#encontra possiveis erros na criacao do usuario

#retorna o usuario criado
	return usuario

try:
	usuario = cadastrar_usuario()
	print('usuario cadastrado com sucesso')
except InvalidEmailError as err:
	print('erro email')

except InvalidAgeError as err:
	print('erro idade')














