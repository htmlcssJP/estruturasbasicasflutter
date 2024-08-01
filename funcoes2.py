# Definindo a função loginUsuario
def loginUsuario(perfil):
    # Verificando se o perfil é 'admin', ignorando maiúsculas e minúsculas
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Chamando a função loginUsuario com diferentes valores de perfil
loginUsuario('etc')