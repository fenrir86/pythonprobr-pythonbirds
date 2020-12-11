# -*- coding: utf-8 -*-
"""
    >>> # Testando motor
    >>> motor=Motor()
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
     >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
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
"""
class Motor:

    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -=2
        self.velocidade = max(0,self.velocidade)

class Direcao:

    posicao = ['Norte','Leste','Sul','Oeste','Norte']
    valor = posicao[0]
    cont = 0
    def __init__(self):
        pass

    def girar_a_direita(self):
        self.cont += 1
        self.valor = self.posicao[self.cont]
    def girar_a_esquerda(self):
        self.cont -= 1
        self.valor = self.posicao[self.cont]

class Carro:
    direcao = Direcao()
    motor = Motor()

    def __init__(self):
        motor = self.motor.velocidade
        self.direcao = direcao

    def calcular_velocidade(self):
        return motor





"""if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)
    print(motor.acelerar())
    direcao= Direcao()
"""