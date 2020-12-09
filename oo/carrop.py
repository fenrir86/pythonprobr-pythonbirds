# -*- coding: utf-8 -*-
"""
    >>> # Testando motor
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
"""
class Motor:
    velocidade = 0
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def cumprimentar(self):
        return f'Olá {id(self)}'

    def acelerar(self):
        self.velocidade += 1

if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)
