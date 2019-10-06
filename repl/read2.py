from symbol2 import Symbol
from cons import Cons


def read2(text):
    """
    >>> read2('()')
    NIL
    >>> read2('NIL')
    NIL
    >>> read2('T')
    T
    >>> read2('t')
    T
    >>> read2('cohadar')
    COHADAR
    >>> read2('(quote x)')
    Cons(QUOTE Cons(X NIL))
    """
    assert text is not None
    t = _Tokens(text)
    ret = t.parse_expr(True)
    if len(t) != 0:
        raise ValueError('extra stuff:' + str(t))
    return ret


class _Tokens():
    def __init__(self, s):
        self.tokens = list(tokenize(s))

    def __len__(self):
        return len(self.tokens)

    def __repr__(self):
        return repr(self.tokens)

    def head(self):
        return self.tokens[0]

    def _next(self):
        self.tokens = self.tokens[1:]

    def _close(self):
        if self.tokens[0] != ')':
            ValueError('not found ")"')
        self._next()

    def parse_expr(self, first=False):
        if self.head() == '(':
            self._next()
            ret = self.parse_etuple()
            self._close()
            return ret
        elif self.head() == ')':
            raise ValueError('unmatched ")"')
        else:
            if first:
                ret = Symbol.get(self.head())  # <---<< symbol
                self._next()
                return ret
            raise ValueError('extra stuff after expression: ' + str(self.tokens))

    def parse_etuple(self):
        if self.head() == '(':
            self._next()
            car = self.parse_etuple()
            self._close()
            return Cons(car, self.parse_etuple())  # <---<< cons
        elif self.head() == ')':
            return Symbol.NIL  # <---<< empty list
        else:
            car = Symbol(self.head())
            self._next()
            return Cons(car, self.parse_etuple())  # <---<< cons


def tokenize(text):
    """
    >>> list(tokenize('()'))
    ['(', ')']

    >>> list(tokenize('foo'))
    ['foo']

    >>> list(tokenize('(foo)'))
    ['(', 'foo', ')']

    >>> list(tokenize('(foo bar)'))
    ['(', 'foo', 'bar', ')']

    >>> list(tokenize('(cdr (quote (a b c)))'))
    ['(', 'cdr', '(', 'quote', '(', 'a', 'b', 'c', ')', ')', ')']
    """
    start = None
    for i, c in enumerate(text):
        if c in [' ', '\t', '\r', '\n']:
            if start is not None:
                yield text[start:i]
                start = None
        elif c in ['(', ')']:
            if start is not None:
                yield text[start:i]
                start = None
            yield c
        else:
            if start is None:
                start = i
    if start is not None:
        yield text[start:]
