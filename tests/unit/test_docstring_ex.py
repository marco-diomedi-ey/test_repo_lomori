import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'project_folder'))

from docstring_ex import somma, conta_unici, primi_fino_a_n


def test_somma():
    """Test minimale per la funzione somma."""
    assert somma(2, 3) == 5
    assert somma(3.5, 4.5) == 8.0


def test_conta_unici():
    """Test minimale per la funzione conta_unici."""
    assert conta_unici([1, 2, 3, 4, 5, 1, 2, 3]) == 5
    assert conta_unici([1, 1, 1]) == 1


def test_primi_fino_a_n():
    """Test minimale per la funzione primi_fino_a_n."""
    risultato = primi_fino_a_n(10)
    assert 2 in risultato
    assert 3 in risultato
    assert 5 in risultato
    assert 7 in risultato