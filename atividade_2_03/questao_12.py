# Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input('Informa a distancia do percurso: '))
velocidade_media = float(input('Innforme a velocidade media esperada para o trajeto: '))

resultado = distancia/velocidade_media

print(f'\nPara concluir esse trajeto sera necessario o total de {resultado} horas')