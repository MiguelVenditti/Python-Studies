"""Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""


print("{:=^40}".format(" LOJAS PERNAMBUCANAS "))

total = float(input("Preço das compras: R$"))
print(''' Formas de Pagamento :
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

while True:
    try:
        escolha = int(input("Qual a sua opção? "))

        if escolha in (1, 2, 3, 4):
            escolha = int(escolha)
            break
        else:
            print("Por favor, selecione uma opção válida.")
    except ValueError:
        print("Por favor, insira um número válido.")

if (escolha == 1):
    novo_valor = total - (total * 10 / 100)
    print("Sua compra de R${:.2f} custará R${:.2f} no final.".format(total,novo_valor))
elif (escolha == 2):
    novo_valor = total - (total * 5 / 100)
    print("Sua compra de R${:.2f} custará R${:.2f} no final.".format(total, novo_valor))
elif (escolha == 3):
    parcela = total / 2
    print("Sua compra de R${:.2f} será paga em duas vezes de R${:.2f}".format(total,parcela))
else:
    vezes = int(input("Quantas vezes deseja parcelar? "))
    novo_valor = total + (total * 20 / 100)
    parcela = novo_valor / vezes
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(vezes,parcela))
    print("Sua compra de R${:.2f} passará a custar R${:.2f} no final".format(total,novo_valor))
