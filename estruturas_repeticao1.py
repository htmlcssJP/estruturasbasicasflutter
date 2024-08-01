# Definindo a variável entrada_idade como uma string vazia
entrada_idade = ''

# Início do loop while
while str(entrada_idade) != '0':
    # Solicitando a entrada do usuário
    entrada_idade = input('Digite um número qualquer ou 0 para sair: ')
    
    # Verificando se o usuário digitou algo diferente de 0 antes de imprimir
    if entrada_idade != '0':
        print(f'Número digitado: {entrada_idade}')
