%M�todo da Bisec��o - Disciplina de C�lculo Num�rico
%Institui��o: Instituto Federal de Pernambuco (IFPE) - Campus Garanhuns
%Autor: Felipe Roque de Albuquerque Neto
%Curso: Bacharelado em Engenharia El�trica

clear
clc

%Recebe a Fun��o desejada
%%disp('Insira a sua fun��o'); Quero que o usuario digite sua funcao
f = @(x)('');%% Digite sua fun��o nesta �rea entre parenteses e aspas simples
%%f = input('Digite a equa��o: ');


%Recebe os Intervalos desejados
xa = input('Insira o valor do Intervalo Xa: '); %Recebe o valor do intervalo A
xb = input('Insira o valor do Intervalo Xb: '); %Recebe o valor do intervalo B

%Recebe a Tolerancia desejada
tolerancia_desejada = input('Insira a tolerancia: '); %Recebe o valor do erro desejado

%Processamento dos Dados
if((f(xa)*f(xb))>0)
    fprintf('Essa fun��o n�o existe');
    
    disp('Insira o valor do Intervalo Xa');
    xa = input('=> '); %Recebe o valor do intervalo A
    disp('Insira o valor do Intervalo Xb: ');
    xb = input('=> '); %Recebe o valor do intervalo B
else
    while(abs(xb-xa)>tolerancia_desejada)
    x_media = (xa+xb)/2;
    if((f(xa)*f(x_media))<0)
        xb = x_media;
    else
        xa = x_media;
    end
    end
end

%Exibindo Resultado da Opera��o
fprintf('A Raiz �: %f',x_media);