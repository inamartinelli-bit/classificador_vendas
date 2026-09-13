import os # Verifica o sistema e limpa a tela
''''''
# os.name =='nt' identifica se o sistema é Windows, executando o comando o comando 'cls' para limpar a tela. 
# Caso contrário (else), para sistemas Linux ou Mac (baseados em Unix), o comando 'clear' é utilizado.
# os.name == 'nt' significa que o sistema operacional é Windows, enquanto 'posix' indica Linux ou Mac.
# os.name retorna 'nt' para Windows e 'posix' para Linux/Mac
''''''
if os.name == 'nt':  # Windows
    os.system('cls')
else:  # Linux/Mac
    os.system('clear')
# Início do programa:
# Este programa classifica o desempenho do vendedor com base em sua porcentagem de vendas realizadas.
print("=" * 25)
print("CLASSIFICADOR DE METAS")
print("=" * 25)
# Entrada de dados pelo usuário. 
# Solicita ao usuário que insira o valor percentual da sua venda.
porcentagem = float(input("Vendedor!\nQual o valor percentual de vendas realizadas (de 0 a 100%): "))
# Processamento dos dados
# Classifica o desempenho do vendedor com base na porcentagem de vendas realizadas.
metabonus = porcentagem >= 100
metafoco = porcentagem < 99 and porcentagem > 80
metaregular = porcentagem < 79 and porcentagem > 50
metabaixo = porcentagem <= 50
# Saída de dados com base na porcentagem de vendas realizadas.
print(f"Percentual de vendas: {porcentagem:.1f}%")
if metabonus:
    print("Excelente! Você atingiu a meta de vendas e ganhou bônus.")
elif metafoco:
    print("Muito bom! Quase lá, mantenha o foco.")
elif metaregular:
    print("Atenção: Desempenho regular. Precisa de melhoria!")
else:
    print("Alerta: Desempenho abaixo do esperado. Procure o gestor.")
# Finalização do programa.