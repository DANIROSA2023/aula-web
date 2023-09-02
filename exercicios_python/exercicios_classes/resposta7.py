class Tamagushi:
    def __init__(self, Nome, Fome = 10, Saude = 0, Idade = 1):
        self.Nome = Nome
        self.Fome = Fome
        self.Saude = Saude
        self.Idade = Idade

    def alt_Nome(self, Nome):
        self.Nome = Nome

    def alt_Fome(self, Fome):
        self.Fome = Fome

    def alt_Saude(self, Saude):
        self.Saude = Saude
        
    def alt_Idade(self, Idade):
        self.Idade = Idade

    def CheckHumor(self): 
        if self.Fome > 7 or self.Saude <= 3:
            return "está mal-humorado"
        else:
            return "está de bom humor"
            
    def DarComida(self):
        if self.Fome <= 10 and self.Fome > 0:
            self.Fome -= 1
            
#Teste Classe
dino = Tamagushi("José")
dino.alt_Nome("João")
dino.alt_Fome(8)
dino.alt_Saude(4)
dino.alt_Idade(9)
dino.DarComida()
dino.DarComida()
dino.DarComida()

print("Nome:",dino.Nome)
print(dino.Fome,"de fome")
print(dino.Saude,"de saúde")
print(dino.Idade,"anos")
print("O bichinho",dino.CheckHumor())