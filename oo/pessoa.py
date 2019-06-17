class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def static_method():
        return 42

class Filho(Pessoa):
    Pessoa.filhos = None


if __name__ == '__main__':
    eder = Pessoa(nome='Eder')
    renzo = Filho(nome='Renzo')
    print(renzo.cumprimentar())
    print(eder.cumprimentar())
    luciano = Pessoa(eder, renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    eder.sobrenome = "pinheiro"
    del renzo.filhos
    renzo.olhos = 1
    print("dict_eder", eder.__dict__)#mostra os atributos de instâncias
    print("dict_renzo", renzo.__dict__)

    print(Pessoa.olhos)
    print(renzo.olhos)
    print(luciano.olhos)
    print(id(Pessoa.olhos), id(renzo.olhos), id(luciano.olhos))

    print(luciano.static_method())
    print(Pessoa.static_method())
