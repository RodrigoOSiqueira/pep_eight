from base import FilaBase

from constantes import CODIGO_NORMAL


class FilaNormal(FilaBase):
	def gera_senha_atual(self):
		self.senha_atual = (
            f'NM{self.codigo}'
        )

	def chama_cliente(self, caixa):
		cliente_atual = self.fila.pop(0)
		self.clientes_atendidos.append(cliente_atual)

		return f'Cliente: {cliente_atual} - Caixa {caixa}'

	def estatistica_detalhada(self, agencia, dia):
		resposta = {}
        resposta['dia'] = dia
        resposta['agencia'] = agencia
        resposta['clientes atendidos'] = len(self.clientes_atendidos)
        resposta['clientes não atendidos'] = len(self.fila)

        return resposta, self.clientes_atendidos
	