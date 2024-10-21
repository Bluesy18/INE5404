from Usuario import Usuario
from fpdf import FPDF
from redefine_controle import redefine_controle
from cadastro_de_usuario import cadastro_de_usuario
from alterar_limites import alterar_limites
from cadastro_de_despesas import cadastro_de_despesas
from data_relatorio import data_relatório
from comparacao import comparacao


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 5, f'Usuário: {usuario.get_nome()}', 0, 1)
        self.set_font('Arial', 'B', 24)
        self.cell(0, 30, f'Relatório do mês {mes_rel.get_mes_ano()}', 0, 1, 'C')

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

    def limites(self, ultrapassados_str, email):
       self.cell(0, 40, f'Os limites de {ultrapassados_str} foram ultrapassados.', 0, 1, 'C')
       self.cell(0, 0, f'Uma notificação será enviada ao email: {email}.' , 0, 1, 'C')

controle = redefine_controle()
lista_meses = []

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
      alterar_limites(lista_meses)

    case "2":
      lista_meses = cadastro_de_despesas(lista_meses)

    case "3":
      ultrapassados = []
      iterador = 0
      mes_rel, mes_comp = data_relatório(lista_meses)
      
      despesa_unica = [["Categoria", "Gasto (R$)", "Data", "Descrição"]]
      despesa_categoria = [["Categoria", "Gasto total (R$)", f"Comparação com mês {mes_comp.get_mes_ano()}"]]
      col_widths1 = [40, 40, 40, 70]
      col_widths2 = [50, 50, 90]
      pdf = PDF()
      for k in list(mes_rel.get_mes_controle().get_categorias().values()):
         for l in k.get_despesas():
          despesa_unica.append([l.get_categoria(), l.get_valor(), l.get_data(), l.get_descricao()])
      for i, j in mes_rel.get_mes_controle().get_categorias().items():
         despesa_categoria.append([f"{i}", f"{j.calcula_valor_total()}", comparacao(mes_rel, mes_comp, iterador)])
         iterador += 1
         if (j.get_ultrapassou() == True):
            ultrapassados.append(j.get_nome())
        
      
      pdf.add_page()
      pdf.create_table(despesa_unica, col_widths1)
      pdf.ln(10) 
      pdf.create_table(despesa_categoria, col_widths2)
      if (len(ultrapassados) != 0):
         pdf.ln(10)
         ultrapassados_str = ", ".join(ultrapassados)
         pdf.limites(ultrapassados_str, usuario.get_email())
      pdf.output('relatorio_mensal.pdf')    

    case "0":
      print("Encerrando sistema...")
      break

    case _:
      print("Operação inválida, tente novamente.")

    

  
  


