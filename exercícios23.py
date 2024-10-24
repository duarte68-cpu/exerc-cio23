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
  def __init__(sef, nome, sobrenome, idade):
    self.nome = nome
    self.sobrenome = sobrenome
    self.idade = idade

nome = aluno(input('digite nome: '))
sobrenome = aluno(input('digite sobrenome: '))
idade = aluno(input('digite idade'))
print('aluno', aluno.nome)
print('aluno', aluno.sobrenome)
print('aluno', aluno.idade)