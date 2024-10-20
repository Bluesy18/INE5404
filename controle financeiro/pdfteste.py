from fpdf import FPDF

class PDF(FPDF):
    def header(self, mes_ano):
        self.mes_ano = mes_ano
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, f'Relatório Financeiro - {self.mes_ano}', 0, 1, 'C')

    def add_category(self, categoria, gasto, limite, comparacao, email):
        # Adiciona categoria com o gasto e limite
        self.set_font('Arial', '', 12)
        if (gasto <= limite):
            status = "Gastos dentro do limite."
        else:
            status = f"Ultrapassou o limite, uma notificação será enviada a {email}"
        comparacao_str = f"Comparação com o mês anterior: {comparacao}"

        self.cell(0, 10, f'{categoria}: R${gasto:.2f} - Limite: R${limite:.2f} - {status}', 0, 1)
        self.cell(0, 10, comparacao_str, 0, 1)
        self.ln(3)

    def total_comparison(self, total_atual, total_anterior):
        # Adiciona a comparação de gastos totais entre os meses
        self.set_font('Arial', 'B', 12)
        if total_atual > total_anterior:
            result = "Gastos totais aumentaram"
        elif total_atual < total_anterior:
            result = "Gastos totais diminuíram"
        else:
            result = "Gastos totais permaneceram iguais"

        self.cell(0, 10, result, 0, 1, 'C')
        self.ln(5)

def gerar_relatorio(mes_ano, despesas_mes_atual, despesas_mes_anterior, limites):
    # Criação do PDF
    pdf = PDF(mes_ano)
    pdf.add_page()

    # Adiciona as despesas categoria por categoria e compara com o mês anterior
    total_mes_atual = sum(despesas_mes_atual.values())
    total_mes_anterior = sum(despesas_mes_anterior.values())

    for categoria, gasto_atual in despesas_mes_atual.items():
        gasto_anterior = despesas_mes_anterior.get(categoria, 0)
        comparacao = "aumentou" if gasto_atual > gasto_anterior else "diminuiu" if gasto_atual < gasto_anterior else "igual"
        limite = limites.get(categoria, 0)  # Pega o limite da categoria
        pdf.add_category(categoria, gasto_atual, limite, comparacao)

    # Comparação dos gastos totais entre os meses
    pdf.total_comparison(total_mes_atual, total_mes_anterior)

    # Salva o PDF
    pdf.output('relatorio_financeiro.pdf')

# Exemplo de uso
despesas_mes_atual = {
    'Educação': 1200.00,
    'Energia': 300.50,
    'Água': 100.00,
    'Transporte': 450.75,
    'Alimentação': 900.00
}

despesas_mes_anterior = {
    'Educação': 1100.00,
    'Energia': 250.00,
    'Água': 100.00,
    'Transporte': 500.00,
    'Alimentação': 950.00
}

limites = {
    'Educação': 1000.00,
    'Energia': 300.00,
    'Água': 150.00,
    'Transporte': 400.00,
    'Alimentação': 850.00
}

mes_ano = 'Setembro 2024'

gerar_relatorio(mes_ano, despesas_mes_atual, despesas_mes_anterior, limites)
