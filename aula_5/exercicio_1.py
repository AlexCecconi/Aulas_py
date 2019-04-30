import datetime 

class Usuario:

	def __init__(self,Nome,Email,Idade):
		self.Nome  = Nome
		self.Email = Email
		self.Idade = Idade
		self.data_criacao = datetime.datetime.now()

	def __str__(self):
		return'{};{};{};{}'format(
			self.Nome
			self.Email
			self.Idade
			self.data_criacao
			)

	def maior_de_idade(self):
		if self.Idade > 17:
			return True
		return False



lucas = Usuario('lucas','a@aaa',26)
alex = Usuario('alex','ll@ll', 30)
# print(lucas.maior_de_idade())
# print(lucas.data_criacao)












exit()
class vetor:
	def __init__(self,x,y):
		self.x=x
		self.y=y

v=vetor(5,2)
u=vetor(2,2)

v.x=10
v.y=20


print(v.y)



exit()
import math

#exercicio de revisao
#escrever uma funcao que recebe
#dois pontos (ou vetores)
#e retorna a soma vetorial

a= (2,1)
b=(3,5)


def soma_vetorial(a,b):
	return a[0]+b[0], a[1]+b[1]
c=soma_vetorial(a,b)
print(c)





# exit()
# import math

# de area_do_circulo(raio, precisao_do_pi=50):
# 	return raio*math.pi

# 	print(area_do_circulo(1))
# 	print(area_do_circulo(5))
# 	print(area_do_circulo(raio=10,precisao_do_pi=20))