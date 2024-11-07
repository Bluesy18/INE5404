from Brinquedo import Brinquedo
from Novo import Novo

class Estoque():
  def __init__(self):
    self.brinquedos = []

  def adicionar_brinquedo(self):
    print("=== ADICIONAR BRINQUEDO ===")
    while True:
      nome = input("Digite o nome do brinquedo: ")
      
      if (nome.isalpha() == True):
        break
      
      else:
        print("Nome inválido, tente novamente.")
    
    while True:
      try:
        preco = float(input("Digite o preço do brinquedo: "))
        break

      except ValueError:
        print("Preço inválido, tente novamente.")

    print("Escolha a faixa etária do brinquedo:\n1 - até 3 anos\n2 - até 5 anos\n3 - até 8 anos\n4 - mais de 8 anos")
    while True:
      faixa_esc = input()
      match faixa_esc:
        case "1":
          faixa_etaria = "até 3 anos"
          break

        case "2":
          faixa_etaria = "até 5 anos"
          break

        case "3":
          faixa_etaria = "até 8 anos"
          break
        case "4":
          faixa_etaria = "mais de 8 anos"
          break

        case _:
          print("Escolha inválida, tente novamente.")

    while True:
      try:
        qtd_estoque = int(input("Digite a quantidade em estoque: "))
        break

      except ValueError:
        print("Quantidade inválida, tente novamente.")

    while True:
      novo = input("O brinquedo é novo? (S/N): ").upper()
      match novo:
        case "S":
          brin = Novo(nome, preco, faixa_etaria, qtd_estoque)
          break

        case "N":
          brin = Brinquedo(nome, preco, faixa_etaria, qtd_estoque)
          break

        case _:
          print("Resposta inválida, tente novamente.")

    self.brinquedos.append(brin)

  def remover_brinquedo(self):
    print("=== REMOVER BRINQUEDO ===")
    nome_rem = input("Digite o nome do brinquedo que você quer deletar: ")
    for _ in self.brinquedos:
      if (nome_rem == _.get_nome()):
        self.brinquedos.remove(_)
        return
      
    print("Nenhum brinquedo com esse nome foi encontrado.")

  def buscar_brinquedo(self):
    print("=== BUSCAR BRINQUEDO ===")

    nome_busca = input("Digite o nome do brinquedo que você está procurando: ")
    for _ in self.brinquedos:
      if (nome_busca == _.get_nome()):
        print(_)
        return
      
    print("Nenhum brinquedo com esse nome foi encontrado.")

  def get_brinquedos(self):
    return self.brinquedos

  