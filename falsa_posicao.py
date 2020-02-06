# Método da Falsa Posição - Cálculo Numérico
# Desenvolvido - Felipe Roque de Albuquerque Neto
# Instituto Federal de Pernambuco - Campus Recife
# Curso de Bacharelado em Engenharia Mecânica

#Importamos a biblioteca de matemática
import math 

# Definição dos intervalos [a,b]
a = float(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
print("\n")

# Definição da tolerancia
e = float(input("Digite o valor da tolerância desejada: "))
print("\n")

# Construção da Funçãa para entrada das equações
def f(x):
    return x**3-x-4 #Equação escolhida

print("a \t\t\t\tb   \t\t\t\tf(a)  \t\t\t\tf(b) \t\t\tXr  \t\t\t\tf(Xr)")
print("\n")

# Teoremo de Bolzano + Cálculo das iterações pelo método da Falsa posição
if(f(a)*f(b)) < 0:
    Xr = ((a*f(b))-(b*f(a)))/(f(b)-f(a))
    while(math.fabs(f(Xr)) > e):
        Xr = ((a*f(b))-(b*f(a)))/(f(b)-f(a))
        print("{} \t\t\t{} \t\t{} \t\t{} \t\t{}".format(a,b,f(a),f(b),Xr))
        if f(Xr) == 0:
            print("A raiz é: ".format(Xr))
        else:
            if f(Xr)*f(a) < 0:
                a = Xr
            else:
                b = Xr
    print("\n")
    print("Valor da raiz é: {}".format(Xr))
    print("\n")
else:
    print("Não há raiz no intervalo informado! Reveja seus dados!")
