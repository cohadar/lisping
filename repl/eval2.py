from symbol2 import Symbol
from cons import Cons
from read2 import read2


def eval2(data):
    """
    >>> eval2(Symbol.NIL)
    NIL

    >>> eval2(Symbol.get('t'))
    T

    >>> eval2(Symbol.get('X'))
    Traceback (most recent call last):
    ValueError: The variable X is unbound.

    >>> eval2(read2('(QUOTE X)'))
    X

    >>> eval2(read2('(QUOTE (A B C))'))
    Cons(A Cons(B Cons(C NIL)))

    >>> eval2(read2('(QUOTE A B)'))
    TODO too many

    >>> eval2(read2('(QUOTE)'))
    TODO too few
    """
    assert isinstance(data, Symbol) or isinstance(data, Cons)
    if data == Symbol.NIL or data == Symbol.get('T'):
        return data
    if isinstance(data, Symbol):
        raise ValueError(f'The variable {data} is unbound.')
    if data.car == Symbol.get('QUOTE'):
        return data.cdr.car
    raise Exception('NYI: ' + str(data))
