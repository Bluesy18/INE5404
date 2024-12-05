import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import os
import json
from datetime import datetime, timedelta
import requests


class TelaBase:    
    def __init__(self, parent):
        self.parent = parent
        self.janela = None

    def abrir(self):
        raise NotImplementedError("Este método deve ser implementado pela classe filha.")

    def fechar(self):
        if self.janela:
            self.janela.destroy()

    def configurar_janela(self, titulo, tamanho):
        self.janela.title(titulo)
        self.janela.geometry(tamanho)


class TelaCadastro(TelaBase):    
    def __init__(self, parent):
        super().__init__(parent)

    def abrir(self):
        self.janela = tk.Toplevel(self.parent)
        self.configurar_janela("Cadastro de Usuário", "300x250")

        tk.Label(self.janela, text="Usuário:").pack(pady=5)
        self.entry_user_cadastro = tk.Entry(self.janela)
        self.entry_user_cadastro.pack(pady=5)

        tk.Label(self.janela, text="Senha:").pack(pady=5)
        self.entry_senha_cadastro = tk.Entry(self.janela, show="*")
        self.entry_senha_cadastro.pack(pady=5)

        tk.Label(self.janela, text="Confirmar Senha:").pack(pady=5)
        self.entry_confirm_senha_cadastro = tk.Entry(self.janela, show="*")
        self.entry_confirm_senha_cadastro.pack(pady=5)

        tk.Button(self.janela, text="Cadastrar", command=self.cadastrar).pack(pady=20)

    def cadastrar(self):
        username = self.entry_user_cadastro.get()
        password = self.entry_senha_cadastro.get()
        confirm_password = self.entry_confirm_senha_cadastro.get()

        if not username or not password or not confirm_password:
            messagebox.showwarning("Erro", "Preencha todos os campos!")
            return

        if password != confirm_password:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return

        if os.path.exists(f"p2/{username}.txt"):
            messagebox.showerror("Erro", "Usuário já cadastrado!")
            return

        with open(f"p2/{username}.txt", "w") as file:
            file.write(password)
        
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        self.fechar()


class TelaLogin(TelaBase):
    def __init__(self, parent):
        super().__init__(parent)

    def abrir(self):
        self.janela = tk.Tk()
        self.configurar_janela("Tela de Login", "300x250")

        tk.Label(self.janela, text="Usuário:").pack(pady=5)
        self.entry_user_login = tk.Entry(self.janela)
        self.entry_user_login.pack(pady=5)

        tk.Label(self.janela, text="Senha:").pack(pady=5)
        self.entry_senha_login = tk.Entry(self.janela, show="*")
        self.entry_senha_login.pack(pady=5)

        tk.Button(self.janela, text="Entrar", command=self.login).pack(pady=10)
        tk.Button(self.janela, text="Cadastrar", command=self.abrir_cadastro).pack()

        self.janela.mainloop()

    def login(self):
        username = self.entry_user_login.get()
        password = self.entry_senha_login.get()

        if not username or not password:
            messagebox.showwarning("Erro", "Preencha todos os campos!")
            return

        if not os.path.exists(f"p2/{username}.txt"):
            messagebox.showerror("Erro", "Usuário não encontrado!")
            return

        with open(f"p2/{username}.txt", "r") as file:
            stored_password = file.read()

        if password == stored_password:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.abrir_selecao_datas()
        else:
            messagebox.showerror("Erro", "Senha incorreta!")

    def abrir_cadastro(self):
        cadastro = TelaCadastro(self.janela)
        cadastro.abrir()

    def abrir_selecao_datas(self):
        self.janela_datas = tk.Toplevel(self.janela)
        self.configurar_janela("Seleção de Datas", "300x250")

        hoje = datetime.today()
        data_limite = hoje + timedelta(days=6)
        hoje_formatada = hoje.strftime("%d/%m/%Y")
        limite_formatada = data_limite.strftime("%d/%m/%Y")

        tk.Label(self.janela_datas, text=f"Selecione a data de início (até {limite_formatada}):").pack(pady=10)
        calendar_inicio = Calendar(self.janela_datas, selectmode="day", date_pattern="dd/mm/yyyy", mindate=hoje, maxdate=data_limite)
        calendar_inicio.pack(pady=10)

        tk.Label(self.janela_datas, text=f"Selecione a data de fim (até {limite_formatada}):").pack(pady=10)
        calendar_fim = Calendar(self.janela_datas, selectmode="day", date_pattern="dd/mm/yyyy", mindate=hoje, maxdate=data_limite)
        calendar_fim.pack(pady=10)

        tk.Button(self.janela_datas, text="Confirmar Datas", command=lambda: self.confirmar_datas(calendar_inicio, calendar_fim)).pack(pady=20)

    def confirmar_datas(self, calendar_inicio, calendar_fim):
        data_inicio = calendar_inicio.get_date()
        data_fim = calendar_fim.get_date()

        hoje = datetime.strptime(data_inicio, "%d/%m/%Y")
        lista_datas = [(hoje + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((datetime.strptime(data_fim, "%d/%m/%Y") - hoje).days + 1)]
        self.abrir_selecao_estado(lista_datas)

    def abrir_selecao_estado(self, datas_validas):
        self.janela_estado = tk.Toplevel(self.janela)
        self.configurar_janela("Seleção de Estado e Capital", "300x400")

        # Carregar dados das capitais
        caminho_capitais = "p2/capitais.json"
        dados_capitais = DadosCapitais(caminho_capitais)

        # Dropdown de estados
        estados = sorted(dados_capitais.capitais.keys())
        tk.Label(self.janela_estado, text="Selecione o estado cuja capital será feita a previsão:").pack(pady=10)
        self.estado_selecionado = tk.StringVar()
        self.estado_selecionado.set(estados[0])  # Primeiro estado como padrão
        dropdown_estado = tk.OptionMenu(self.janela_estado, self.estado_selecionado, *estados)
        dropdown_estado.pack(pady=10)

        # Exibir a capital correspondente
        self.label_capital = tk.Label(self.janela_estado, text="")
        self.label_capital.pack(pady=10)

        # Botão de confirmar
        tk.Button(self.janela_estado, text="Confirmar", command=lambda: self.confirmar_estado(datas_validas, dados_capitais)).pack(pady=20)

    def confirmar_estado(self, datas_validas, dados_capitais):
        estado = self.estado_selecionado.get()
        capital_info = dados_capitais.capitais.get(estado, {})
        latitude = capital_info.get("latitude")
        longitude = capital_info.get("longitude")

        if latitude is None or longitude is None:
            messagebox.showerror("Erro", "Dados da capital não encontrados.")
            return

        # Fazer previsão
        previsao = Previsao(latitude, longitude, datas_validas, estado)
        previsoes = previsao.fazer_previsao()

        if previsoes:
            exibir_conteudo_json(previsoes)
        self.janela_estado.destroy()

class DadosCapitais:    
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.capitais = self.carregar_capitais()

    def carregar_capitais(self):
        try:
            with open(self.caminho_arquivo, "r", encoding="utf-8") as file:
                data = json.load(file)
            return {capital["estado"]: capital for capital in data["capitais"]}
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo 'capitais.json' não encontrado.")
            exit()
        except json.JSONDecodeError:
            messagebox.showerror("Erro", "Erro ao ler o arquivo 'capitais.json'.")
            exit()


class Previsao:    
    def __init__(self, latitude, longitude, datas_validas, cont):
        self.latitude = latitude
        self.longitude = longitude
        self.datas_validas = datas_validas
        self.cont = cont

    def fazer_previsao(self):
        base_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_mean",
            "timezone": "America/Sao_Paulo"
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()

            data = response.json()
            previsoes = []

            for day, temp_max, temp_min, precip_prob in zip(
                data["daily"]["time"],
                data["daily"]["temperature_2m_max"],
                data["daily"]["temperature_2m_min"],
                data["daily"]["precipitation_probability_mean"]
            ):
                if day in self.datas_validas:
                    previsoes.append({
                        "data": day,
                        "temperatura_maxima": temp_max,
                        "temperatura_minima": temp_min,
                        "probabilidade_precipitacao": precip_prob
                    })

            if previsoes:
                filename = f"p2/previsoes_{self.cont}.json"
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(previsoes, f, ensure_ascii=False, indent=4)

                messagebox.showinfo("Sucesso", f"Previsões salvas em {filename}")
                return previsoes

            else:
                messagebox.showwarning("Aviso", "Não há previsões para os dias selecionados.")
                return None
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao consultar a API: {e}")
            return None


def exibir_conteudo_json(previsoes):
    janela_json = tk.Toplevel()
    janela_json.title("Previsões")
    janela_json.geometry("600x400")
    frame = tk.Frame(janela_json)
    frame.pack(pady=20)

    for previsao in previsoes:
        data = previsao["data"]
        temp_max = previsao["temperatura_maxima"]
        temp_min = previsao["temperatura_minima"]
        precip_prob = previsao["probabilidade_precipitacao"]

        label = tk.Label(frame, text=f"Data: {data} | Temp Máx: {temp_max}°C | Temp Mín: {temp_min}°C | Prob. Precipitação: {precip_prob}%")
        label.pack(anchor="w")



login = TelaLogin(None)
login.abrir()
