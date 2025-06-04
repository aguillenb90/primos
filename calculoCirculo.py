import numpy as np

def area_circulo(radio):
    """
    Calcula el área de un círculo usando NumPy.
    
    Parámetros:
    radio (float o array): Radio del círculo (puede ser un número o un array de radios)
    
    Retorna:
    float o array: Área(s) del/los círculo(s)
    
    Ejemplo:
    >>> area_circulo(5)
    78.53981633974483
    
    >>> area_circulo(np.array([1, 2, 3]))
    array([ 3.14159265, 12.56637061, 28.27433388])
    """
    return np.pi * radio ** 2


# Para un solo círculo
print(area_circulo(2))  # 12.566370614359172

