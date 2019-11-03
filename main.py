from constantes import FILA_NORMAL, FILA_PRIORITARIA
from estatistica_detalhada import EstatisticaDetalhada
from fabrica_fila import FabricaFila


fila_priori = FabricaFila(FILA_PRIORITARIA).pega_fila()

fila_priori.atualiza_fila_template()
fila_priori.atualiza_fila_template()
fila_priori.atualiza_fila_template()
fila_priori.atualiza_fila_template()
fila_priori.atualiza_fila_template()
fila_priori.atualiza_fila_template()
fila_priori.atualiza_fila_template()
fila_priori.atualiza_fila_template()
fila_priori.atualiza_fila_template()
fila_priori.atualiza_fila_template()
print(fila_priori.chama_cliente(10))
print(fila_priori.chama_cliente(10))
print(fila_priori.chama_cliente(10))
print(fila_priori.chama_cliente(10))
print(fila_priori.chama_cliente(10))
print(fila_priori.chama_cliente(10))
print(fila_priori.chama_cliente(10))
print(fila_priori.chama_cliente(10))
print(fila_priori.chama_cliente(10))
print(fila_priori.chama_cliente(10))

print(fila_priori.estatistica('03/11/2019', 6058, EstatisticaDetalhada))