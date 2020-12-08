# -*- coding: utf-8 -*-

class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome =None, idade=33 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_statico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return  f'{cls} - {cls.olhos} '

if __name__ == '__main__':
    p = Pessoa()
    filho = Pessoa(nome='Emilio')
    mae =  Pessoa(filho, nome='Ivone')
   # print(Pessoa.cumprimentar(p))
   # print(id(p))
   # print(p.cumprimentar())
    p.nome = 'Emilio'
    print(p.nome,p.idade)
    for familia in mae.filhos:
        print(familia.nome)
    print(Pessoa.metodo_statico(),filho.metodo_statico())
    print(Pessoa.nome_e_atributos_de_classe(),filho.nome_e_atributos_de_classe())