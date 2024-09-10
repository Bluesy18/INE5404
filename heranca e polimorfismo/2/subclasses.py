from classes import Ingresso

class VIP(Ingresso):
    def __init__(self):
        super().__init__()
        self.valor = self.valor+10

class Normal(Ingresso):
    def __init__(self):
        super().__init__()

    def normal(self):
        print("Ingresso Normal")

