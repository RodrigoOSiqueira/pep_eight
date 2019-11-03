class EstatisticaDetalhada:
	def __init__(self, agencia, dia):
		self._agencia = agencia
		self._dia = dia

	def roda_estatistica(self, clientes):
		resposta = {}
		resposta['dia'] = self._dia
		resposta['agencia'] = self._agencia
		resposta['quantidade de clientes atendidos'] = len(clientes)
		resposta['clientes atendidos'] = clientes

		return resposta
