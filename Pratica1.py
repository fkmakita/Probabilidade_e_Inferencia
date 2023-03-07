# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 23:55:50 2022

@author: fabio
"""


#%% Importação de bibliotecas e configuração de diretório

import matplotlib.pyplot as plt
import numpy as np
import os
import scipy.io as sc
import statistics as st
import scipy.stats as ss

# Direcionamento do diretório das imagens
#os.chdir(r'E:\Arquivos\ENGENHARIA MÉDICA - PRES\Atividade Prática 1')


#%% Leitura e extração inicial de dados

A1 = sc.loadmat('Atividade 1')
A2 = sc.loadmat('Atividade 2')

D1 = A1['dados']
D2 = A2['dados']

#%% Atividade 1 - Distribuição Gaussiana e a Síndrome do Túnel do Carpo

#%% Atividade 1 - A

mCMAP_avg = round(st.mean(D1[0]), 2)
mSNAP_avg = round(st.mean(D1[1]), 2)
uCMAP_avg = round(st.mean(D1[2]), 2)
uSNAP_avg = round(st.mean(D1[3]), 2)

D_avg = [mCMAP_avg, mSNAP_avg, uCMAP_avg, uSNAP_avg]

mCMAP_std = round(st.variance(D1[0]), 2)
mSNAP_std = round(st.variance(D1[1]), 2)
uCMAP_std = round(st.variance(D1[2]), 2)
uSNAP_std = round(st.variance(D1[3]), 2)

D_std = [mCMAP_std, mSNAP_std, uCMAP_std, uSNAP_std]


#%% Atividade 1 - B

'''
Teste de Shapiro Wilk tem como hipótese nula que a distribuição é uma Gaussiana
primeiro parâmetro de retorno: resultado do teste
segundo parâmetro de retorno: p-value

Caso o p-value seja menor que 5%, rejeitamos a hipótese de que a distribuição seja
uma Gaussiana
'''

plt.title('Histograma mCMAP - 0')
plt.grid('on')
plt.xlim((50, 65))
plt.ylim((0, 40))
plt.hist(D1[0], bins = 10)
print('Resultado do teste de Shapiro-Wilk: ' + str(round(ss.shapiro(D1[0])[0]*100, 2)) + '%\np value: ' + str(round(ss.shapiro(D1[0])[1]*100, 2)) + '%')

plt.title('Histograma mSNAP - 1')
plt.grid('on')
plt.xlim((40, 60))
plt.ylim((0, 50))
plt.hist(D1[1], bins = 10)
print('Resultado do teste de Shapiro-Wilk: ' + str(round(ss.shapiro(D1[1])[0]*100, 2)) + '%\np value: ' + str(round(ss.shapiro(D1[1])[1]*100, 2)) + '%')

plt.title('Histograma uCMAP - 2')
plt.grid('on')
plt.xlim((50, 60))
plt.ylim((0, 40))
plt.hist(D1[2], bins = 10)
print('Resultado do teste de Shapiro-Wilk: ' + str(round(ss.shapiro(D1[2])[0]*100, 2)) + '%\np value: ' + str(round(ss.shapiro(D1[2])[1]*100, 2)) + '%')

plt.title('Histograma uSNAP - 3')
plt.grid('on')
plt.xlim((55, 65))
plt.ylim((0, 35))
plt.hist(D1[3], bins = 10)
print('Resultado do teste de Shapiro-Wilk: ' + str(round(ss.shapiro(D1[3])[0]*100, 2)) + '%\np value: ' + str(round(ss.shapiro(D1[3])[1]*100, 2)) + '%')


#%% Atividade 1 - C

D_paciente = [56, 52, 54, 61]

plt.title('Medida 1')
plt.grid('on')
plt.ylim((0, 40))
plt.xlim((50, 65))
plt.vlines(x = D_paciente[0], ymin = -0.2*min(D1[0]), ymax = 1.2*max(D1[0]), colors = 'r', linestyles = '--')
plt.hist(D1[0], bins = 10)

plt.title('Medida 2')
plt.grid('on')
plt.ylim((0, 50))
plt.xlim((40, 60))
plt.vlines(x = D_paciente[1], ymin = -0.2*min(D1[1]), ymax = 1.2*max(D1[1]), colors = 'r', linestyles = '--')
plt.hist(D1[1], bins = 10)

plt.title('Medida 3')
plt.grid('on')
plt.ylim((0, 40))
plt.xlim((50, 60))
plt.vlines(x = D_paciente[2], ymin = -0.2*min(D1[2]), ymax = 1.2*max(D1[2]), colors = 'r', linestyles = '--')
plt.hist(D1[2], bins = 10)

plt.title('Medida 4')
plt.grid('on')
plt.ylim((0, 35))
plt.xlim((55, 65))
plt.vlines(x = D_paciente[3], ymin = -0.2*min(D1[3]), ymax = 1.2*max(D1[3]), colors = 'r', linestyles = '--')
plt.hist(D1[3], bins = 10)


#%% Atividade 1 - D

mCMAP_cdf = ss.norm.cdf(D_paciente[0], loc = D_avg[0], scale = D_std[0])
mSNAP_cdf = ss.norm.cdf(D_paciente[1], loc = D_avg[1], scale = D_std[1])
uCMAP_cdf = ss.norm.cdf(D_paciente[2], loc = D_avg[2], scale = D_std[2])
uSNAP_cdf = ss.norm.cdf(D_paciente[3], loc = D_avg[3], scale = D_std[3])

D_cdf = [mCMAP_cdf, mSNAP_cdf, uCMAP_cdf, uSNAP_cdf]

print('Resultado do teste da distribuição normal cumulada mCMAP: ' + str(round(D_cdf[0]*100, 2)) + '%')
print('Resultado do teste da distribuição normal cumulada mSNAP: ' + str(round(D_cdf[1]*100, 2)) + '%')
print('Resultado do teste da distribuição normal cumulada uCMAP: ' + str(round(D_cdf[2]*100, 2)) + '%')
print('Resultado do teste da distribuição normal cumulada uSNAP: ' + str(round(D_cdf[3]*100, 2)) + '%')

'''
Comparando o resultado do teste de CDF, o indivíduo tem resultados muito superiores ao
limiar de 5% proposto no exercício. Assim, não podemos rejeitar a hipótese do paciente
ser saudável.
'''


#%% Atividade 1 - E

covar_matr = np.cov((D1[0], D1[1], D1[2], D1[3]))

multivar = ss.multivariate_normal.cdf(D_paciente, mean = D_avg, cov = covar_matr)

print('Resultado do teste da distribuição multivariada CDF: ' + str(round(multivar*100, 2)) + '%')

'''
Com o teste da distribuição multivariada CDF abaixo do limiar de 5%,
podemos agora rejeitar a hipótese do paciente ser saudável.
'''


#%% Atividade 2 - Inferência e Testes Diagnósticos

# Agora iremos trabalhar com a Matriz de Dados D2, 1 = Doente, 0 = Saudável
# Coluna 1: PSA; Coluna 2: DRE; Coluna 3: Biopsia

#%% Atividade 2 - A
# Calcular a sensibilidade do teste PSA e DRE => P( T = 1 | D = 1 )

# Obtenção dos subtotais dos indivíduos PSA e BIO
popul = len(D2[:,0])
PSA1 = np.sum(D2[:,0])
PSA0 = popul - PSA1
BIO1 = np.sum(D2[:,2])
BIO0 = popul - BIO1

Prob_BIO1 = BIO1/popul


PSA1BIO1 = 0
for i in range(popul):
    if D2[i,0] == 1 and D2[i,2] == 1:
        PSA1BIO1 += 1

matriz_PSA = np.matrix([['-', 'Doença', 'Não Doença', '-'],
         ['Teste', PSA1BIO1, PSA1 - PSA1BIO1, PSA1],
         ['Não Teste', BIO1 - PSA1BIO1, PSA0 - (BIO1 - PSA1BIO1), PSA0],
         ['-', BIO1, BIO0, '-']])

Prob_PSA1_Dado_BIO1 = int(matriz_PSA[1, 1])/int(matriz_PSA[3, 1])

print('Resultado da sensibilidade do teste PSA: ' + str(round(Prob_PSA1_Dado_BIO1*100,2)) + '%')

# Obtenção dos subtotais dos indivíduos DRE
DRE1 = np.sum(D2[:,1])
DRE0 = popul - DRE1

DRE1BIO1 = 0
for i in range(popul):
    if D2[i,1] == 1 and D2[i,2] == 1:
        DRE1BIO1 += 1

matriz_DRE = np.matrix([['-', 'Doença', 'Não Doença', '-'],
         ['Teste', DRE1BIO1, DRE1 - DRE1BIO1, DRE1],
         ['Não Teste', BIO1 - DRE1BIO1, DRE0 - (BIO1 - DRE1BIO1), DRE0],
         ['-', BIO1, BIO0, '-']])

Prob_DRE1_Dado_BIO1 = int(matriz_DRE[1, 1])/int(matriz_DRE[3, 1])

print('Resultado da sensibilidade do teste DRE: ' + str(round(Prob_DRE1_Dado_BIO1*100,2)) + '%')


#%% Atividade 2 - B
# Estimar a especificidade dos testes PSA e DRE => P( T = 0 | D = 0)

Prob_PSA0_Dado_BIO0 = int(matriz_PSA[2, 2])/int(matriz_PSA[3, 2])

Prob_DRE0_Dado_BIO0 = int(matriz_DRE[2, 2])/int(matriz_DRE[3, 2])

print('Resultado da especificidade do teste PSA: ' + str(round(Prob_PSA0_Dado_BIO0*100,2)) + '%')

print('Resultado da especificidade do teste DRE: ' + str(round(Prob_DRE0_Dado_BIO0*100,2)) + '%')


#%% Atividade 2 - C
# Aplicação do Teorema de Bayes
# Calcular P( D = 1 | T = 1 )
# P( D = 1 | T = 1 ) = P( T = 1 | D = 1 ) * P( D = 1 ) / P( T = 1 )

# Inferência para o teste PSA
Prob_D = 0.042
Prob_PSA1 = Prob_PSA1_Dado_BIO1*Prob_D + (1 - Prob_PSA0_Dado_BIO0)*(1 - Prob_D)

Prob_BIO1_Dado_PSA1 = Prob_PSA1_Dado_BIO1 * Prob_D / Prob_PSA1

print('Prob de ter a doença dado PSA positivo: ' + str(round(Prob_BIO1_Dado_PSA1*100,2)) + '%')

# Inferência para o teste DRE

Prob_DRE1 = Prob_DRE1_Dado_BIO1*Prob_D + (1 - Prob_DRE0_Dado_BIO0)*(1 - Prob_D)

Prob_BIO1_Dado_DRE1 = Prob_DRE1_Dado_BIO1 * Prob_D / Prob_DRE1

print('Prob de ter a doença dado DRE positivo: ' + str(round(Prob_BIO1_Dado_DRE1*100,2)) + '%')


'''
CONFERIR MAIS TARDE
'''

#%% Atividade 2 - D
# Calcular a probabilidade combinada para doença dado que ambos os testes foram positivos
# P( D = 1 | PSA = 1, DRE = 1 ) = P( PSA = 1, DRE = 1 | D = 1 ) * P( D = 1 ) / P( PSA = 1, DRE = 1 )

PSA1DRE1 = 0
PSA1DRE1BIO1 = 0
for i in range(popul):
    if D2[i,0] == 1 and D2[i,1] == 1:
        PSA1DRE1 += 1
    if D2[i,0] == 1 and D2[i,1] == 1 and D2[i,2] == 1:
        PSA1DRE1BIO1 += 1

matriz_PSA_DRE = np.matrix([['-', 'Doença', 'Não Doença', '-'],
                            ['Testes', PSA1DRE1BIO1, PSA1DRE1 - PSA1DRE1BIO1, PSA1DRE1],
                            ['Não Testes', BIO1 - PSA1DRE1BIO1, BIO0 - (PSA1DRE1 - PSA1DRE1BIO1), popul - PSA1DRE1],
                            ['-', BIO1, BIO0, '-']])

matriz_DRE = np.matrix([['-', 'Doença', 'Não Doença', '-'],
         ['Teste', DRE1BIO1, DRE1 - DRE1BIO1, DRE1],
         ['Não Teste', BIO1 - DRE1BIO1, DRE0 - (BIO1 - DRE1BIO1), DRE0],
         ['-', BIO1, BIO0, '-']])



# Calcular a probabilidade combinada para doença dado que pelo menos um teste é positivo
# P( D = 1 | PSA = 1, DRE = 0) + P( D = 1 | PSA = 1, DRE = 1) + P( D = 1 | PSA = 0, DRE = 1)

Prob_PSA1_ou_DRE1 = (Prob_BIO1_Dado_PSA1*(1-Prob_DRE1) +
                     Prob_BIO1_Dado_PSA1*Prob_DRE1 +
                     Prob_BIO1_Dado_DRE1*Prob_PSA1 +
                     Prob_BIO1_Dado_DRE1*(1-Prob_PSA1))

Prob_D/(Prob_PSA1*Prob_DRE1)


