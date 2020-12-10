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

    direita = ['Norte','Leste','Sul','Oeste']
    def __init__(self,valor):
        self.valor = valor

    def girar_a_direita(self):
        cont = 0
        #valor=self.valor
        while (self.direita[cont]==0):
            direcao.valor = self.direita[cont]
            cont +=1


    def girar_a_esquerda(self):
        pass


if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)
    print(motor.acelerar())
    direcao= Direcao()
