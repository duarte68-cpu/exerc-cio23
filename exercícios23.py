exercicio = input ('digite o opções 1 e 2: ')

if exercicio == '1':

 nome = input('digite seu nome: ')
 sobrenome = input('digite seu sobrenome: ')
 idade = input('digite sua idade: ')
 lista = [nome, sobrenome, idade]
print(lista[0])
print(lista[1])
print(lista[2])

elif exercicio == '2':
 numero = int(input('informe mês de 1 a 12: '))
 lista = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
print(lista[numero - 1])
else:
   print('opção invalida')
   
   
  
class aluno():
    def __init__(self, nome, sobrenome, idade, cidade):
     self.nome = nome
     self.sobrenome = sobrenome
     self.idade = idade
     self.cidade = cidade

nome = input('digite nome: ')
sobrenome = input('digite sobrenome: ')
idade = int(input('digite idade: '))
cidade = input('cidade de origem: ')
outros = aluno(nome, sobrenome, idade, cidade)
print(f'aluno: {outros.nome}')
print(f'sobrenome: {outros.sobrenome}')
print(f'idade: {outros.idade}')
print(f'cidade: {outros.cidade}')



class contaBancaria:

       def __init__(self, nome, conta, saldo):
           self.nome = nome
           self.conta = conta
           self.saldo = float(saldo)

       def deposito(self):
           self.saldo = 1000 + self.saldo


       def bancaria(self):
           print(f'\nnome do usuário {self.nome}')
           print(f'conta bancária {self.conta}')
           print(f'saldo em conta {self.saldo}')



conta_1 = contaBancaria(input('Nome do titular da conta: '), input('numero conta corrente: '), input('valor deposito: '))
conta_1.deposito()
conta_1.bancaria()
