from symbol2 import Symbol


def read2(text):
    assert text is not None
    """
    >>> Read()('()')
    NIL
    >>> Read()('NIL')
    NIL
    >>> Read()('T')
    T
    >>> Read()('t')
    T
    >>> Read()('cohadar')
    COHADAR
    """
    if text == 'T':
        return Symbol.get('T')
    if text in ['()', 'NIL']:
        return Symbol.NIL
    return Symbol.get(text)
