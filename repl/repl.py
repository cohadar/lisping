from read import Read
from eval import Eval
from print import Print

_read = Read()
_eval = Eval()
_print = Print()


def repl(text):
    """
    >>> repl('()')
    NIL
    >>> repl('NIL')
    NIL
    >>> repl('T')
    T
    >>> repl('X')
    The variable X is unbound.
    """
    return print(_print(_eval(_read(text))))
