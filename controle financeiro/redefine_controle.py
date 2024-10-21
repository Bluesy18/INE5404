from Categoria import Categoria
from ControleFinanceiro import ControleFinanceiro

def redefine_controle():
  educacao = Categoria("Educação")
  energia = Categoria("Energia")
  agua = Categoria("Água")
  internet = Categoria("Internet")
  alimentacao = Categoria("Alimentação")
  transporte = Categoria("Transporte")
  residencia = Categoria("Residência")
  entretenimento = Categoria("Entretenimento")

  controle = ControleFinanceiro({educacao.get_nome(): educacao,
                                energia.get_nome(): energia,
                                agua.get_nome(): agua,
                                internet.get_nome(): internet,
                                alimentacao.get_nome(): alimentacao,
                                transporte.get_nome(): transporte,
                                residencia.get_nome(): residencia,
                                entretenimento.get_nome(): entretenimento,})
  
  return controle