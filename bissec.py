# Método da Bisecção: Disciplina de Cálculo Numérico
# Autor: Felipe Roque de Albuquerque Neto
# Instituição: Instituto Federal de Pernambuco - Campus Recife
# Curso: Bacharelado em Engenharia Mecânica

#Importamos a biblioteca de matemática
import math 

# Definição dos intervalos [a,b]
a = float(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
print("\n")

# Definição da tolerancia
e = float(input("Digite a tolerancia desejada: "))
print("\n")

# Construção da Função para entrada das equações
def f(x):
    return x**2 +math.log(x) # Inserimos aqui nossa equação escolhida
print("a \tb   \t\tx_media   \t\t\tf(a) \t\t\t\tf(b)                   \t\t\tf(x_media)")
print("\n")

# Teoremo de Bolzano
if (f(a)*f(b)) < 0:
    while (math.fabs(b-a)/2 > e):
        x_media = (a+b)/2
        print("{} \t{}\t\t{}    \t\t{} \t\t{}                           \t\t{}".format(a,b,x_media,f(a),f(b),f(x_media)))
        if f(x_media) == 0:
            print(" A Raiz é: {}".format(x_media))
        else:
            if f(a)*f(x_media) < 0:
                b = x_media
            else: 
                a = x_media
    print("\n")
    print("Valor da raiz é: {} ".format(x_media))
    print("\n")
else:
    print("Não há raiz neste intervalo!")
