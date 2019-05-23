# Vinho Verde

Teste realizado para a cognitivo.ai, com o objetivo de criar um modelo para estimar a qualidade do vinho, com base em de vinhos portugueses "Vinho Verde", que possuem variantes de vinho branco e tinto. Devido a questões de privacidade, apenas variáveis físico-químicas (input) e sensoriais (output) estão disponíveis (por exemplo, não há dados sobre tipo de uva, marca do vinho, preço de venda, etc).

## Instruções

A análise exploratória está no notebook **01_eda.ipynb** e o modelo está em **02_model.ipynb**. O arquivo **utils.py** contém funções auxiliares usadas na exploratória e na modelagem. As bibliotecas utilizadas estão listadas no **requirements.txt**, e a versão do Python usada foi a 3.6.8

## Como foi a definição da sua estratégia de modelagem?

A estratégia foi baseada no tipo de problema (aprendizado supervisionado) e nas características dos preditores e resposta presentes na base. Como existe correlação entre preditores, usei um modelo com regularização para evitar que os coeficientes "estourassem", prejudicando a qualidade da predição. E, por se tratar de um problema de regressão onde não haviam dados para toda a amplitude possível da resposta, considerei que um modelo linear seria a melhor opção pois é possível extrapolar a reta ajustada para prever valores que não foram observados no treino.

## Como foi definida a função de custo utilizada?

A função de custo não precisou ser definida, pois é parte do modelo *ElasticNet*, não podendo ser escolhida / customizada:

![](assets/elastic.png)

## Qual foi o critério utilizado na seleção do modelo final?

Os hiperparâmetros foram selecionados dentro de um processo de validação cruzada *k-fold* com k=5. A base de treino é separada em 5 partes de mesmo tamanho, e a cada passo da validação os modelos são ajustados em uma combinação de 4 dessas partes, e avaliados na parte restante. O melhor modelo é selecionado de acordo com o valor do *Erro Quadrático Médio* em cima da "parte restante", que é a base de validação, e reajustado com os hiperparâmetros escolhidos em cima de toda a base de treino (ou seja, das 5 partes combinadas).

## Qual foi o critério utilizado para validação do modelo? Por que escolheu utilizar este método?

Além do processo de validação cruzada, a *Raíz do Erro Quadrático Médio (RMSE)* foi usada para avaliar o desempenho na base de treino e na base de teste, para identificar se houve overfitting e avaliar a qualidade da previsão, dado que o *RMSE* mede o quão longe nossas previsões estão do valor real.

## Quais evidências você possui de que seu modelo é suficientemente bom?

Calculei o *RMSE* de dois modelos aleatórios, usando a mediana e a média de **quality** na base de treino como previsão para a base de teste. O modelo *ElasticNet* prevê valores mais próximos aos reais em comparação a esses modelos. Por se tratar de uma base onde a resposta é baseada em critérios subjetivos e fatores que não estavam disponíveis como preditores (como vinícola e preço, por exemplo), considero que o resultado foi bom o suficiente.
