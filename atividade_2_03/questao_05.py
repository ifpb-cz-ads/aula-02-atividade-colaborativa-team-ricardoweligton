# Escreva uma expressao para determinar se uma pessoa deve ou nao pagar imposto. Considere que pagam imposto pessoas cujo salario e maior que R$ 1.200,00

salario = float(input('Informe o salario: '))

if salario > 1200:
    print('A pessoa deve pagar imposto')
else:
    print('A pessoa nao deve pagar imposto')