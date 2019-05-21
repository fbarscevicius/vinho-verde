from typing import Union

_FLOAT_OR_STR = Union[float, str]


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
