# Método da Bisecção: Disciplina de Cálculo Numérico
# Autor: Felipe Roque de Albuquerque Neto
# Instituição: Instituto Federal de Pernambuco - Campus Recife
# Curso: Bacharelado em Engenharia Mecânica

#OBS: Lembre que antes de inserir a equação neste programa
# precisas manipula-la da forma f(x) = x para x = f(x)

# Bibliotecas
import math

# Função que receberá nossa Equação:
def f(x):
    return (math.sin(x) + math.cos(x))/2 # Inserir a equação aqui


def ponto_fixo(f,x,tol):
    erro = 1
    iteracao = 0

    while erro > tol:
        x_novo = f(x)
        erro = abs(x_novo-x)
        x = x_novo
        iteracao +=1
        print(f'x{iteracao} = {x: 0.6f}') # Printa as iterações feitas
    print('\n')

    # Printa o Resultado final
    print(f'Raiz Encontrada: {x: 0.6f}\nQuantidade Iteracões Feitas: {iteracao}') 
    print('\n')
ponto_fixo(f, 10, 0.001)
