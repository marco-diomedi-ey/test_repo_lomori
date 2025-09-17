def somma(a, b):
    """
    Somma due numeri.
    
    Parameters
    ----------
    a: int or float

    b: int or float

    Returns
    -------
    int or float
        La somma di a e b.
    """
    return a + b


def conta_unici(lista):
    """
    Conta il numero di elementi unici in una lista.
    
    Parameters
    ----------
    lista: list
        La lista di elementi da scorrere
    
    Returns
    -------
    int
        Il numero di elementi unici nella lista.
    """
    return len(set(lista))


def primi_fino_a_n(n):
    """
    Restituisce una lista di numeri primi da 1 a n.

    Parameters
    ----------
    n: int
        Il numero fino a cui cercare i numeri primi.
    
    Returns
    -------
    list
        Una lista di numeri primi da 1 a n.

    """
    original_n = [2, 3, 5, 7]
    c = []
    for i in range(1, n+1):
        if (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0) or (i in original_n):
            c.append(i)
    return c