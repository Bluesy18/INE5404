from subclasses import Novo, Velho

while True:
    cond = input("Seu imóvel é (V)elho ou (N)ovo?: ").upper()

    match cond:
        case "V":
            i = Velho()
            print(f"Seu imóvel tem o desconto de R$ {i.get_desconto()}.")
            break
        case "N":
            i = Novo()
            print(f"Seu imóvel tem o acréscimo de R$ {i.get_acrescimo()}.")
            break
        case _:
            print("Tente novamente.")

print(f"Seu imóvel é em {i.get_endereco()}")
print(f"Seu imóvel custa {i.get_valor()}")