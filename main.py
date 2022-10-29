"Calculadora Python com 2 valores"

valor1 = float(input('Digite o Primeiro valor da Operação!'))
valor2 = float(input('Digite o segundo valor da Operação!'))
operacao = input('Digite a operação desejada(+, -, *, /)')

if operacao == '+':
    res = valor1 + valor2
elif operacao == '-':
    res = valor1 - valor2
elif operacao == '*':
    res = valor1 * valor2
elif operacao == '/':
    res = valor1 / valor2
else:
    print('Operação digitada é invalida')
    res = 0
print('Resultado:', res)
