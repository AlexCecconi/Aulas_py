import banco

#Exercicio1:
#Imprima somente os usuaris
#cujs emails contenham as letras:
#'a' ou 'k' ou 'm' ou 'l'
#E as idades entre 30 e 40

Template = '{nome};{idade};{email};{sexo};{endereco}';

for usuario in banco.lista_de_usuarios:
	email = usuario['email'].lower()
	condicao1= 'a' in email
	
	condicao1= condicao1 or 'k' in email
	condicao1=condicao1 or 'm' in email
	condicao1=condicao1 or 'l' in email

	idade = usuario['idade']
	condicao2= idade > 30 and idade < 40

	if  condicao1 and condicao2:
		print(usuario)








