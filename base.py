import abc


class FilaBase(metaclass=abc.ABCMeta):
	codigo = None
	fila = []
	clientes_atendidos = []
	senha_atual = None

	def atualiza_fila(self):
		self.reseta_fila()
		self.gera_senha_atual()
		self.atualiza_fila()

	@abc.abstractmethod
	def gera_senha_atual(self):
		...

	@abc.abstractmethod
	def chama_cliente(self, caixa):
		...

	@abc.abstractmethod
	def estatistica_detalhada(self, agencia, dia):
		...

	def estatistica_resumida(self, agencia, dia):
		quantidade_atendimentos = len(
			self.clientes_atendidos
		)

		return  (
			f'{agencia} - {dia}: '
			f'{quantidade_atendimentos} clientes atendidos'
		)	

	def reseta_fila(self):
		if self.codigo >= 100:
            self.codigo = 0

	def atualiza_fila(self):
        self.fila.append(self.senha_atual)
