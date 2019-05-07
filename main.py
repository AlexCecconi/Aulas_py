import banco

print(banco.lista_de_usuarios)


exit()
TEMPLATE = '{nome};{idade};{email};{sexo};{endereco}';

for usuario in lista_de_usuarios:
	if usuario['idade'] > 30:
		print(TEMPLATE.format(
							nome=usuario['nome'],
							idade=usuario['idade'],
							email=usuario['email'],
							sexo=usuario['sexo'],
							endereco=usuario['endereco']

))



exit()
mensagem = 'Olá {nome}, seja bem vindo ao mundo do python'
mensagem = mensagem.format(nome='Alex')
print(mensagem)







exit()
n = 3
fib = 0 
i = 1
j= 0

for x in range(n):
	fib = i+j
	i=j
	j=fib



print(fib)







#n-1 + n-2
exit()
nome = input('qual vai se  a melhor lnguagem:')

if nome == 'Python':
	print('Voce acertou')
	print("Alex")
else:
	print('errou : (')


















































