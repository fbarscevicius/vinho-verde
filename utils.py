import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error
from typing import Union

_FLOAT_OR_STR    = Union[float, str]
_SERIES_OR_ARRAY = Union[pd.core.series.Series, np.ndarray]


def convert_alcohol_str(x: _FLOAT_OR_STR) -> float: 
    """
    Converte os valores do preditor `alcohol` para float,
    cuidando dos casos com formatação inconsistente. Utilizar
    no método `apply` do pd.DataFrame
    
    Args:
        x (float or str): observação no DataFrame

    Returns:
        Valor de `x` convertido para `float`
    """    
    
    try:
        x = float(x)
        
    except ValueError:
        x = x[:2] + '.' + x[2]
        x = float(x)
        
        if x > 50:
            x /= 10

    return x


def bivariate_plot(ncol: int, nrow: int, data: pd.DataFrame, target: str) -> None:
    """
    Plota um grid de gráficos de barra mostrando a relação entre
    cada preditor do DataFrame com a resposta
    
    Args:
        ncol (int): número de colunas do grid
        nrol (int): número de linhas do grid
        data (pd.DataFrame): base de dados
        target (str): nome da variável resposta
    """
    
    fig, axs = plt.subplots(nrows=nrow, ncols=ncol, figsize=(16, 24))
    axs = axs.flatten()
    
    for idx, ax in enumerate(axs):
        sns.barplot(x=data.loc[:, target], y=data.iloc[:, idx], ax=ax);

    plt.tight_layout();
    plt.show();
    plt.gcf().clear();
    
    
def univariate_plot(ncol: int, nrow: int, data: pd.DataFrame, target: list) -> None:
    """
    Plota um grid de gráficos de distribuição para as variáveis selecionadas
    
    Args:
        ncol (int): número de colunas do grid
        nrol (int): número de linhas do grid
        data (pd.DataFrame): base de dados
        target (list): lista de variáveis a serem plotadas
    """
     
    fig, axs = plt.subplots(nrows=nrow, ncols=ncol, figsize=(16, 24))
    axs = axs.flatten()
    
    for idx, var in enumerate(target):
        sns.distplot(data[var], ax=axs[idx]);

    plt.tight_layout();
    plt.show();
    plt.gcf().clear();
    
    
def get_coefs(colnames: list, coefs: np.ndarray, sort: bool = True) -> pd.DataFrame:
    """
    Retorna um DataFrame com duas colunas: (nome da variável, valor do coeficiente)
    
    Args:
        colnames (list): nomes das variáveis
        coefs (array): coeficientes retornados pelo modelo
        sort (bool): ordenar o retorno de acordo com abs(coefs)

    Returns:
        DataFrame
    """
    
    out = list(zip(colnames, coefs))
    
    if sort:
        out.sort(key=lambda x: abs(x[1]), reverse=True)
        
    return pd.DataFrame(out, columns=['variavel', 'valor'])


def rmse(y_true: _SERIES_OR_ARRAY, y_pred: _SERIES_OR_ARRAY) -> float:
    """
    Calcula a Raíz do Erro Quadrático Médio
    
    Args:
        y_true (pd.Series or np.ndarray): vetor de respostas observadas
        y_pred (pd.Series or np.ndarray): vetor de respostas preditas
        
    Returns:
        valor do RMSE
    """
    
    return mean_squared_error(y_true, y_pred)**0.5


def plot_coef_hbar(data: pd.DataFrame) -> None:
    """
    Plota barras horizontais dos coeficientes do modelo
    
    Args:
        data (pd.DataFrame): DataFrame retornado pela função `get_coefs`
    """
    plt.figure(figsize=(10, 8))
    plt.barh(data.variavel, data.valor)
    plt.title('Variável x Coeficiente')