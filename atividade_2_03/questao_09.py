# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuario. Calcule o total em segundos

dias = int(input('Informe uma quantidade de dias: '))
horas = int(input('Informe uma quantidade de horas: '))
minutos = int(input('Informe uma quantidade de minutos: '))
segundos = int(input('Informe uma quantidade de segundos: '))

total_segundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + (segundos)

print('{} dias, {} horas, {} minutos e {} segundos, equivalem a {} segundos'.format(dias, horas, minutos, segundos, total_segundos))