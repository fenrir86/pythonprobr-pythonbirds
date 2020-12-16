# -*- coding: utf-8 -*-

class Pessoa:

    def __init__(self, *filhos, nome =None, idade=33 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'

    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass

if __name__ == '__main__':
    p = Pessoa()
    filho = Homem(nome='Emilio')
    mae =  Pessoa(filho, nome='Ivone')
   # print(Pessoa.cumprimentar(p))
   # print(id(p))
   # print(p.cumprimentar())
    p.nome = 'Emilio'
    print(p.nome,p.idade)
    for familia in mae.filhos:
        print(familia.nome)
    pessoa= Pessoa('Anonimo')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa, Homem))