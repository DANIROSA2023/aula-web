class Bombacombustivel:


    def __init__(self, tipo_combustivel, valor_litro, quant_combustivel=0):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quant_combustivel = quant_combustivel

    
    def abastecer_por_valor(self, valor):
        resultado = valor / self.valor_litro
        self.quant_combustivel -= resultado
        return (f"Valor pago R${valor}, quantidade abastecida: {resultado:.2f}L")
        
    
    def abastecer_por_litro(self, valor):
        resultado = valor * self.valor_litro
        self.quant_combustivel -= resultado
        return (f"Valor pago R${valor}, quantidade abastecida: {resultado}L")

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    def alterar_quant_combustivel(self, quantidade):
        self.quant_combustivel = quantidade




b1 = Bombacombustivel("gasolina", 6, 19)
print(b1.abastecer_por_valor(19))

        

    