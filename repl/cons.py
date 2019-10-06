class Cons():
    """
    >>> Cons('njak', 'zrak')
    ('njak' 'zrak')
    >>> Cons('njak', 'zrak').car
    'njak'
    >>> Cons('njak', 'zrak').cdr
    'zrak'
    """
    def __init__(self, car, cdr):
        assert car is not None
        assert cdr is not None
        self._car = car
        self._cdr = cdr

    @property
    def car(self):
        return self._car

    @property
    def cdr(self):
        return self._cdr

    def __repr__(self):
        return '({!r} {!r})'.format(self._car, self._cdr)
