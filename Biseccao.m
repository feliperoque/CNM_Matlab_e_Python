%Método da Bisecção - Disciplina de Cálculo Numérico
%Instituição: Instituto Federal de Pernambuco (IFPE) - Campus Garanhuns
%Autor: Felipe Roque de Albuquerque Neto
%Curso: Bacharelado em Engenharia Elétrica

%Recebe a Função desejada
f = @(x) x^2+log(x);%% Digite sua função nesta área entre parenteses e aspas simples

%Recebe os Intervalos desejados
xa = input('Insira o valor do Intervalo Xa: '); %Recebe o valor do intervalo A
xb = input('Insira o valor do Intervalo Xb: '); %Recebe o valor do intervalo B

%Recebe a Tolerancia desejada
tolerancia_desejada = input('Insira a tolerancia: '); %Recebe o valor do erro desejado

%Processamento de Dados
disp('I      Xa          Xb        X_media      f(Xa)       f(Xb)');
if f(xa)*f(xb)>0
    fprintf('Não existe raiz o intervalo inserido!');
    return
else
    while(abs(xb-xa)>tolerancia_desejada)
    i = i + 1;%Contator de iterações
    x_media = (xa+xb)/2;
    fprintf('%d \t%f \t%f \t%f \t%f \t%f \n',i,xa,xb,x_media,f(xa),f(xb));
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
