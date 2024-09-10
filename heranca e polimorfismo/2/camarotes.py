from subclasses import VIP
import random

class CamaroteInferior(VIP):
    def __init__(self):
        super().__init__()
        setores = ["Setor Norte", "Setor Leste", "Setor Sul", "Setor Oeste"]
        self.local = random.choice(setores)

    def get_local(self):
        return self.local
    
class CamaroteSuperior(VIP):
    def __init__(self):
        super().__init__()
        self.valor = self.valor+5

    