from enum import InitEnum

from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria


@unique
class TiposFila(InitEnum):
	fila_normal = 1
	fila_prioritaria = 2


class FabricaFila:
	def __init__(self, tipo_fila):	
		self._tipo_fila = tipo_fila

	def pega_fila(self):
		if self.tipo_fila == TiposFila.fila_normal:
			return FilaNormal()
		if self.tipo_fila == TiposFila.fila_prioritaria:
			return FilaPrioritaria()
		else:
			raise NotImplementedError('Tipo não cadastrado')
