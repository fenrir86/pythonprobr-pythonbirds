# -*- coding: utf-8 -*-

class Pessoa:

    def __init__(self, nome = None):
        self.none = None

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
   # print(Pessoa.cumprimentar(p))
   # print(id(p))
   # print(p.cumprimentar())
    p.nome = 'Emilio'
    print(p.nome)