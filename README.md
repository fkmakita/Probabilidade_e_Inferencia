# Probabilidade e Inferência Estatística
## Laboratório 1 de Engenharia Médica
<br>
Síndrome do Túnel do Carpo
<br>
No laboratório 1 de Engenharia Médica realizamos testes estatísticos para verificar a normalidade da distribuição de dados biológicos para o diagnóstico de Síndrome do Túnel do Carpo (STC). A STC pode ser associada a uma redução na velocidade de condução nervosa, armazenadas na matriz do arquivo "Atividade 1.mat".
<br><br>
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/223552653-5ed76f92-8bac-4c3b-a899-86bc6575fabb.png" width = 300>
</p>
<br>
Cada linha da matriz (4 linhas (medidas) vs 200 colunas (indivíduos)) representa um tipo de medida:<br><br>
Linha 1: medida de condução motora (CMAP) do nervo mediano (mCMAP);<br>
Linha 2: medida de condução sensorial (SNAP) do nervo mediano (mSNAP);<br> 
Linha 3: CMAP do nervo ulnar (uCMAP);<br>
Linha 4: SNAP do nervo ulnar (uSNAP).<br><br>

Em um primeiro momento, foi realizado um histograma de cada medida, destacando com uma linha pontilhada vermelha a situação de um paciente específico com medidas: mCMAP = 56 m/s; mSNAP = 52 m/s; uCMAP = 54 m/s; uSNAP = 61 m/s. No eixo x temos a velocidade de condução de cada medida e no eixo y a quantidade de indivíduos em cada bin.<br><br>

<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/223556115-628c97c1-d170-4831-9f94-a56dd99c4f2a.png" height = 220>
<img src = "https://user-images.githubusercontent.com/86500603/223556580-5141cb27-2915-4c61-b5b1-f6bdfa95c4ea.png" height = 220>
</p>
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/223556590-e687989a-d27b-404f-bae1-93b9ddf1e751.png" height = 220>
<img src = "https://user-images.githubusercontent.com/86500603/223556601-e88f0608-ce0a-4ed8-ad61-2fca00fd93f6.png" height = 220>
</p>

Em seguida, foi realizado um teste estatístico de Shapiro-Wilk (biblioteca scipy.stats) para testar a normalidade das distribuições. O resultado obtido foi superior ao p-value de 5% pré estabelecido, assim não foi possível rejeitar a hipótese de normalidade.<br><br>

<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/223557305-9c3dcc52-eb6f-4970-b087-8d3a5a6c5229.png" height = 120>
</p>

Dando sequência, foram realizados testes para cada variável isoladamente, com o intuito de verificar a hipótese do paciente (destacado em vermelho anteriormente) ser saudável dentro de um limiar de 5% com a função normcdf (biblioteca scipy.stats). O resultado obtido foi superior ao limiar de 5% pré estabelecido, assim não foi possível rejeitar a hipótese de que o paciente seja saudável.

<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/223560914-8f6c03de-cc02-4857-b27f-571756262bd2.png" height = 60>
</p>

Para finalizar, foi realizado um teste similar ao anterior, alterando o tipo de univariada para multivariada através do uso da matriz de covariância. Agora, o resultado obtido foi inferior ao limiar de 5%, assim podendo rejeitar a hipótese do paciente ser saudável.<br><br>

Sensibilidade e Especificidade
<br>
O cálculo de sensibilidade (prob de teste positivo DADO QUE o indivíduo possui a doença) e especificidade (prob de teste negativo DADO QUE o indivíduo não possui a doença) é de grande importância para avaliar a eficácia de um teste/diagnóstico. Para isso, trabalhamos com o arquivo "Atividade 2.mat", que contém dados de 19476 homens de +50 anos e que foram submetidos a testes de câncer de próstata. Os testes realizados foram separados em 3:
<br><br>
Coluna 1: resultado do teste PSA (1 - positivo para doença, 0 - negativo para doença)<br>
Coluna 2: resultado do teste de toque retal (DRE) (1 - positivo para doença, 0 - negativo para doença)<br>
Coluna 3: resultado da biópsia (padrão ouro) (1 - positivo para doença, 0 - negativo para doença)<br>
<br>
Foi estimado o valor de sensibilidade e especificidade para cada teste baseado na amostra de 19476 homens, obtendo os seguintes resultados:
<br>
PSA: sensibilidade 25,57%, especificidade 94,91%<br>
DRE: sensibilidade 17,76%, especificidade 93,5%<br>
<br>
Além disso, foram explorados os primeiros conceitos de inferência estatística e Teorema de Bayes, que serão melhor ilustrados em outras atividades.
