import exercicio_1

USUARIOS = []

def cadastrar_usuario():

	nome=input('digite seu nome:')
	email=input('digite seu email')
	idade = int(input('digite sua idade'))

u = exercicio_1.usuario(nome, email, idade)
USUARIOS.append(u)

def listar_usuarios():
	with opne('relatorio.csv','w') as arquivo:
		for u in USUARIOS:
			arquivo.write(str(u)+'/n')


done = False
while not done:

	print('1-criar usuario')
	print('2-lista usuario')
	print('3-salvar usuarios(csv)')

	option = int(input('selecione uma das opcoes acima: '))

	if option == 1:
		cadastrar_usuario()
	elif option == 2:	
		listar_usuario()
	else:
		done = True	

print(' Xau : ) ')