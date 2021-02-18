# Faca um programa que solicite o preco de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preco a pagar

preco = float(input('Informe o preco: '))
desconto = float(input('Informe o percentual de desconto: '))

valor_desconto = preco * (desconto/100)
novo_preco = preco - valor_desconto

print('O desconto eh de R${} e o novo preco a se pagar eh de R${}'.format(valor_desconto, novo_preco))