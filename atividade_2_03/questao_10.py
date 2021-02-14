# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário

salario = float(input('Informe o valor do salario: '))
aumento = float(input('Informe a porcentagem do aumento: '))

resultado = salario + (salario * aumento/100)
print(f'Apos o aumento de {aumento}% no salario, o salario atual eh de R$ {resultado}')