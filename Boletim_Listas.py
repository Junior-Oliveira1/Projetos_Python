#crie um programa que leia nome e duas notas de varios alunos e guarde tudo em
#uma lista composta. no final mostre um boletim contendo a média de cada um e permita que o usuario
#possa mostrar as notas de cada aluno individualmente

alunos = []

while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2]])
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-'*20)
print(f'{"No.":<4}{"Nome":<15}{"Média":>8}')
print('-'*40)

for i, a in enumerate(alunos):
    media = (a[1][0] + a[1][1]) / 2
    print(f'{i:<4}{a[0]:<15}{media:8.2f}')
print('=-'*40)

while True:
    opcao = int(input('Digite o número do aluno que deseja ver as notas. (999 interrompe o programa): '))
    print('-' * 40)
    if opcao == 999:
        print('Programa encerrado')
        break
    if 0 <= opcao < len(alunos):
        print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]}')
    else:
        print('Aluno não encontrado! Tente novamente.')
    print('-' * 40)

