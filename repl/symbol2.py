class Symbol():
    interned = {}
    NIL = None

    def __init__(self, name):
        """
        >>> Symbol(None)
        Traceback (most recent call last):
        AssertionError

        >>> Symbol('njak'); Symbol('njak')
        Traceback (most recent call last):
        AssertionError: NJAK

        >>> Symbol('zrak')
        ZRAK
        """
        assert name is not None
        uname = name.upper()
        assert uname not in Symbol.interned, uname
        self.name = uname
        Symbol.interned[self.name] = self

    @classmethod
    def get(cls, name):
        """
        >>> Symbol.get('foo')
        FOO

        >>> Symbol.get('bar') == Symbol.get('bar')
        True

        >>> Symbol.get('foo') != Symbol.get('bar')
        True
        """
        uname = name.upper()
        ret = Symbol.interned.get(uname)
        return ret if ret is not None else Symbol(uname)

    def __repr__(self):
        """
        >>> Symbol('lalala')
        LALALA
        """
        return self.name


Symbol.NIL = Symbol.get('NIL')
