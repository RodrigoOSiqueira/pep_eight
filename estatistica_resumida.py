class EstatisticaDetalhada:
	def __init__(self, agencia, dia):
		self._agencia = agencia
		self._dia = dia

	def roda_estatistica(self, clientes):
		quantidade_atendimentos = len(
			clientes
		)

		return  (
			f'{self._agencia} - {self._dia}: '
			f'{quantidade_atendimentos} clientes atendidos'
		)
