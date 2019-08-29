%Método da Bisecção - Disciplina de Cálculo Numérico
%Instituição: Instituto Federal de Pernambuco (IFPE) - Campus Garanhuns
%Autor: Felipe Roque de Albuquerque Neto
%Curso: Bacharelado em Engenharia Elétrica

clear
clc

%Recebe a Função desejada
f = @(x) ;%% Digite sua função nesta área após @(x)

%Recebe os Intervalos desejados
xa = input('Insira o valor do Intervalo Xa: '); %Recebe o valor do intervalo A
xb = input('Insira o valor do Intervalo Xb: '); %Recebe o valor do intervalo B

%Recebe a Tolerancia desejada
tolerancia_desejada = input('Insira a tolerancia: '); %Recebe o valor do erro desejado

%Processamento dos Dados
if((f(xa)*f(xb))>0)
    fprintf('Não existe raiz o intervalo inserido!');
    return
else
    while(abs(xb-xa)>tolerancia_desejada)
    x_media = (xa+xb)/2;
    if((f(xa)*f(x_media))<0)
        xb = x_media;
    else
        xa = x_media;
    end
     if abs(f(xa))<tolerancia_desejada
        break
    end
    end
end

%Exibindo Resultado da Operação
fprintf('A Raiz é: %f',x_media);
