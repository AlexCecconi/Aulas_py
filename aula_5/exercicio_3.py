class ContaBancaria:
	self.rendimento=0.02
	self.quantidade=0.00



	def sacar(self,quantidade):
		print('sacar {}'.format(quantidade))

	def retirar(self,quantidade):
		print('retirar {}'.format(quantidade))

	def calcular_rendimento(self):
		pass

class ContaCorrente(ContaBancaria):
	pass

conta = ContaCorrente()
conta.sacar(100)








