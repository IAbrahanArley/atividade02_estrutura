""" Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método
chamado “calcular_area” que retorna a área do retângulo. """

class Retandgulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    
    def calcular_area(self):
        return self.base * self.altura

r1 = Retandgulo(10, 10)
print(r1.calcular_area())
r1.calcular_area()