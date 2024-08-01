# Definindo a variável saida
saida = ''

# Função que realiza a adição
def adicao(a, b):
    return a + b

# Função que realiza a subtração
def subracao(a, b):
    return a - b

# Função que realiza a multiplicação
def multiplicacao(a, b):
    return a * b

# Função que realiza a divisão, com verificação de divisão por zero
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

# Função calculadora que decide qual operação realizar
def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao':
        resultado = subracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado

# Laço while para continuar ou encerrar o programa
while saida.lower() != 'n':
    # Solicitando os números e a operação ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /) ou o nome da operação: ")

    # Chamando a função calculadora
    resultado = calculadora(num1, num2, operacao)

    # Exibindo o resultado
    print(f'Resultado da operação: {resultado}')

    # Perguntando se o usuário deseja continuar ou sair
    saida = input("Deseja continuar? Digite S para sim ou N para não: ")

    # Informando ao usuário que a resposta é insensível a maiúsculas e minúsculas
    if saida.lower() != 's':
        print("Programa encerrado.")
