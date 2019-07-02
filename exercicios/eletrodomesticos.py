class Eletrodomestico:
    def liga(self):
        raise NotImplementedError


class Microonda(Eletrodomestico):

    def liga(self):
        return 'Microondas ligado'


class MaquinaDeLavar(Eletrodomestico):

    def liga(self):
            return 'Máquina de lavar ligada'

class Casa():

    def __init__(self):
        self._my_e = [Eletrodomestico] * 0

    def adiciona_eletrodomestido(self, eletro):
        self._my_e.append(eletro)

    def liga_tudo(self):
        return ', '.join(e.liga() for e in self._my_e)


if __name__ == '__main__':
    minha_casa = Casa()
    meu_microonda = Microonda()
    minha_maquina_de_lavar = MaquinaDeLavar()
    minha_casa.adiciona_eletrodomestido(meu_microonda)
    minha_casa.adiciona_eletrodomestido(minha_maquina_de_lavar)
    print(minha_casa.liga_tudo())