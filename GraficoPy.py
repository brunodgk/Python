#Código para fazer um exemplo de gráfico 2D simples em python, por Brunodgk 2017

#Importando bibliotecas e dando nome de variáveis
import numpy as np;
import matplotlib.pyplot as plt;

#Cálculo Exemplificado para fazer o Gráfico
data1 = [10,5,2,4,6,8];
data2 = [ 1,2,4,8,7,4];
x = 10*np.array(range(len(data1)));

#Plotação do Gráfico
plt.plot( x, data1, 'go'); #Bola verde
plt.plot( x, data1, ':', color='orange'); #Linha Pontilha Laranja
plt.plot( x, data2, 'r^'); #Triangulo Vermelho
plt.plot( x, data2, '--', color='blue');  #Linha Tracejada Azul

#Tamanho dos Eixos e o Título do Gráfico
plt.axis([-10, 60, 0, 11]);
plt.title("Gráfico Teste em Python");

#Grade e Nomenclatura dos eixos no gráfico Cartesiano
plt.grid(True);
plt.xlabel("Eixo X Horizontal");
plt.ylabel("Eixo Y Vertical");
plt.show();
