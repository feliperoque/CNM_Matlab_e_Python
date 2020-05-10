# Método da Bisecção: Disciplina de Cálculo Numérico
# Autor: Felipe Roque de Albuquerque Neto
# Instituição: Instituto Federal de Pernambuco - Campus Recife
# Curso: Bacharelado em Engenharia Mecânica

#OBS: Lembre que antes de inserir a equação neste programa
# precisas manipula-la da forma f(x) = x para x = f(x)

# Bibliotecas
import math

# Nossa função
def f(x):
    return x**2 + math.log(x)

x = float(input("Valor Inicial: "))
e = float(input("Tolerancia: "))
print("\n")

i = 0
x_anterior = 0

while (abs(x - x_anterior) > e):
    x_anterior = x
    x = f(x)

    print(i, "{0:.6f}".format(x), "{0:.6f}".format(abs(x - x_anterior)))
    i = i+1
