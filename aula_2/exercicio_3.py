
arquivo = open('relatorio.csv','r')
for linha in arquivo.readlines()
	registro = linha.split(';')
	usuario = {
		'nome'  :    registro[0]
		'idade' :    registro[1]
		'email' :    registro[2]
		'sexo'  :    registro[3]
		'endereco' : registro[4]
	}

exit()
arquivo = open('usuario.txt','r')
for linha in arquivo.readlines():
	print(linha)
arquivo.close()	

arquivo = open('teste.txt','w')
arquivo.write('hello, word')
arquivo.close()

arquivo = open('usuario.txt', 'r')
for linha in arquivo.readlines();
	print(linha)
arquivo.close()

arquivo = open()