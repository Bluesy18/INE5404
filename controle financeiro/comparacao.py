def comparacao(mes_rel, mes_comp, iterador):
   lista_rel = list(mes_rel.get_mes_controle().get_categorias().values())
   lista_comp = list(mes_comp.get_mes_controle().get_categorias().values())
   dif = lista_rel[iterador].calcula_valor_total() - lista_comp[iterador].calcula_valor_total()

   if (dif > 0):
      return f"Acréscimo de R${dif}."
   
   elif(dif < 0):
      dif = dif*(-1)
      return f"Decréscimo de R${dif}."
   
   else:
      return "Não houve mudança."