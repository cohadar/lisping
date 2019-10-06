from read2 import read2
from eval2 import eval2
from print2 import print2


def repl(text):
    """
    >>> repl('()')
    NIL
    >>> repl('NIL')
    NIL
    >>> repl('T')
    T
    >>> repl('X')
    Traceback (most recent call last):
    ValueError: The variable X is unbound.
    """
    return print2(eval2(read2(text)))
