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
