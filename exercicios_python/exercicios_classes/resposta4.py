class Pessoa:
    def __init__(self,nome,idade,peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        return self.idade
    def engordar(self, kilos):
        self.peso += kilos
        return self.peso
    def emagrecer(self,kilos_perdidos):
        self.peso -= kilos_perdidos
        return self.peso

    def crescer(self,anos):
        if self.idade<21:
            self.altura += (0.05)*anos
        return self.altura
Maria = Pessoa('Maria', 19, 68, 1.76)
print(Maria.__dict__)
print(f'seu nome é {Maria.nome}, você tem {Maria.idade} anos, pesa {Maria.peso} kgs e tem uma altura de {Maria.altura}')

Maria.envelhecer(1)
Maria.crescer(2)                    
                                   
Maria.engordar(10)

print(Maria.__dict__)
print(f'seu nome é {Maria.nome}, você tem {Maria.idade} anos, pesa {Maria.peso} kgs e tem uma altura de {Maria.altura}')

Maria.emagrecer(5)

print(Maria.__dict__)
print(f'seu nome é {Maria.nome}, você tem {Maria.idade} anos, pesa {Maria.peso} kgs e tem uma altura de {Maria.altura}')
