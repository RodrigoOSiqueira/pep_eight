from base import FilaBase

from constantes import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):
	def gera_senha_atual(self):
		self.senha_atual = (
            f'PR{self.codigo}'
        )

	def chama_cliente(self, caixa):
		display = []
		cliente_atual = self.fila.pop(0)
		display.append(f'Cliente: ]{cliente_atual} - Caixa {caixa}')

		if len(self.fila) >= 3:
			display.append(f'Próximo: {self.fila[0]}')
			display.append(f'Fique atento: {self.fila[1]}')

		self.clientes_atendidos.append(cliente_atual)

		return display

	def estatistica_detalhada(self, agencia, dia):
		resposta = {}
        resposta['dia'] = dia
        resposta['agencia'] = agencia
        resposta['clientes atendidos'] = len(self.clientes_atendidos)
        resposta['clientes não atendidos'] = len(self.fila)

        return resposta, self.clientes_atendidos
