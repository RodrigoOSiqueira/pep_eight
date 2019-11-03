import abc


class FilaBase(metaclass=abc.ABCMeta):
	codigo = 0
	fila = []
	clientes_atendidos = []
	senha_atual = None

	def atualiza_fila_template(self):
		self.reseta_fila()
		self.gera_senha_atual()
		self.atualiza_fila()

	@abc.abstractmethod
	def gera_senha_atual(self):
		...

	@abc.abstractmethod
	def chama_cliente(self, caixa):
		...

	def reseta_fila(self):
		if self.codigo >= 100:
			self.codigo = 0
		else:
			self.codigo += 1

	def atualiza_fila(self):
		self.fila.append(self.senha_atual)
