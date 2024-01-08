print('Exercício')
grade = input('Qual a nota do aluno? ')
try:
    nota_int=float(grade)
    if nota_int >= 0.9:
        print('A nota é A')
    elif nota_int >=0.8:
        print('A nota é B')
    elif nota_int >=0.7:
        print('A nota é C')
    else:
        print(' O aluno rodou. A nota é D')
except:
    print('Você precisa fornecer um número entre 0 e 1')

