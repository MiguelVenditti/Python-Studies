"""Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias
notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor."""


def notas(* num, sit=False):
    """
    - Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionario com várias informações sobre a situação da turma.
    """

    aluno = dict()
    aluno['total'] = len(num)
    aluno['maior'] = 0
    aluno['menor'] = 999
    aluno['media'] = sum(num) / len(num)

    # validando as maior e menos nota

    for x in num:
        if (x > aluno['maior']):
            aluno['maior'] = x
        elif (x < aluno['menor']):
            aluno['menor'] = x

    # Validando a situação do aluno
    if (sit):
        if (aluno['media'] < 5):
            aluno['situação'] = 'RUIM'
        elif (aluno['media'] >= 5 and aluno['media'] < 7):
            aluno['situação'] = 'RAZOAVEL'
        else:
            aluno['situação'] = 'BOA'

    return aluno

resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
