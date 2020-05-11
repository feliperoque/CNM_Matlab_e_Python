# Método da Bisecção: Disciplina de Cálculo Numérico
# Autor: Felipe Roque de Albuquerque Neto
# Instituição: Instituto Federal de Pernambuco - Campus Recife
# Curso: Bacharelado em Engenharia Mecânica

#OBS: Lembre que antes de inserir a equação neste programa
# precisas manipula-la da forma f(x) = x para x = f(x)

# Bibliotecas
import math

# Função do cálculo do Ponto_Fixo
def ponto_fixo(x0, erro, n_de_iteracoes):
    x1 = f(x0)
    if (abs(x1-x0)<erro):
        return x1

    iteracao = 0

    while ((n_de_iteracoes > iteracao) and (abs(x1-x0) > = erro)):
        iteracao+=1


