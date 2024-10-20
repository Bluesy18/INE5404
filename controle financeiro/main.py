from Despesa import Despesa
from Categoria import Categoria
from ControleFinanceiro import ControleFinanceiro
from Usuario import Usuario
from fpdf import FPDF
from cadastro_de_usuario import cadastro_de_usuario
from alterar_limites import alterar_limites
from cadastro_de_despesas import cadastro_de_despesas
from data_relatorio import data_relatório
import math
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 5, f'Usuário: {usuario.get_nome()}', 0, 1)
        self.set_font('Arial', 'B', 24)
        self.cell(0, 30, f'Relatório do mês {mes_rel}', 0, 1, 'C')

    def create_table(self, data, col_widths):
        self.set_font('Arial', 'B', 12)
        for col in data[0]:
            self.cell(col_widths[data[0].index(col)], 10, col, 1)
        self.ln()
        
        self.set_font('Arial', '', 12)
        for row in data[1:]:
            for col in row:
                self.cell(col_widths[row.index(col)], 10, str(col), 1)
            self.ln()

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

first = True

while True:
  print("=== SISTEMA DE CONTROLE FINANCEIRO ===")
  if (first == True):
    usuario = Usuario(*cadastro_de_usuario())
  
  first = False

  print("DIGITE A OPERAÇÃO QUE DESEJA REALIZAR:\n1 - ALTERAR LIMITES\n2 - CADASTRAR DESPESAS\n3 - GERAR RELATÓRIO\n0 - ENCERRAR SISTEMA")
  op = input()

  match op:
    
    case "1":
      alterar_limites(controle)

    case "2":
      cadastro_de_despesas(controle)

    case "3":
      mes_rel, mes_comp = data_relatório(controle)
      
      despesa_unica = [["Categoria", "Gasto (R$)", "Data", "Descrição"]]
      despesa_categoria = [["Categoria", "Gasto total (R$)", f"Comparação com mês {mes_comp}"]]
      col_widths1 = [40, 40, 40, 70]
      col_widths2 = [50, 50, 90]
      pdf = PDF()
      for g in list(controle.get_meses().values()):
        for l in g:
          despesa_unica.append([l.get_categoria(), l.get_valor(), l.get_data(), l.get_descricao()])    
      for i, k in controle.get_categorias().items():
        despesa_categoria.append([f"{i}", f"{k.despesas_total()}"])
      pdf.add_page()
      pdf.create_table(despesa_unica, col_widths1)
      pdf.ln(10) 
      pdf.create_table(despesa_categoria, col_widths2)
      pdf.output('relatorio_mensal.pdf')

    case "0":
      print("Encerrando sistema...")
      break

    case _:
      print("Operação inválida, tente novamente.")

    

  
  


