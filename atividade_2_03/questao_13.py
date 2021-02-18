# Escreva um programa que converta uma temperatura digitada em °C em °F. A formula para essa conversao eh: F = 9 × C ÷ 5 + 32

temp_celsius = float(input('Informe a temperatura em Celsius: '))
temp_fahrenheit = 9 * temp_celsius / 5 + 32

print('{} graus Celsius equivalem a {} graus Fahrenheit'.format(temp_celsius, temp_fahrenheit))