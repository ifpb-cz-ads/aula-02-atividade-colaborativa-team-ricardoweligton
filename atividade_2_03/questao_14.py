# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado

km_rodados = float(input('Informe a quantos kilometros foram percorridos pelo carro: '))
total_dias_aluguel = float(input('Informe quantos dias o carro foi alugado: '))

resultado = km_rodados * 0.15 + total_dias_aluguel * 60

print(f'O valor final a pagar pelo aluguel do carro eh de R$ {resultado}')