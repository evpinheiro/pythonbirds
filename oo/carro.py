"""
Criar classe carro composta por duas classes
1) Motor - objetiva controlar a valocidade
    * Atributo velocidade
    * Método acelerar: incrementar a velocidade em uma unidade
    * Método frear: decrementar a velocidade em duas unidade

2) Direção - controla a direção
    * Valor de direção: Norte, Sul, Leste, Oeste
    * Metodo girar_a_direita
    * Metodo girar_a_esquerda
        N
      O   L
        S

    Exemplo:
    #Testanto motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> #Testanto Direção
    >>> direcao = Direcao()
    >>> direcao.valor()
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor()
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor()
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor()
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor()
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor()
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor()
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor()
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor()
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'

"""
class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def calcular_direcao(self):
        return self.direcao.valor()

class Motor:

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade = max(0, self.velocidade-2)

class Direcao:
    DIRECOES = ('Norte', 'Leste', 'Sul', 'Oeste')
    def __init__(self):
        self.direcao = 0

    def girar_a_direita(self):
        self.direcao = (self.direcao + 1) % 4;

    def girar_a_esquerda(self):
        self.direcao = (self.direcao - 1) % 4;

    def valor(self):
        return self.DIRECOES[self.direcao]

