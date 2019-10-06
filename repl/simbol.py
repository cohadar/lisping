class Simbol():
    interned = {}
    NIL = None

    def __init__(self, name):
        """
        >>> Simbol(None)
        Traceback (most recent call last):
        AssertionError
        >>> Simbol('njak'); Simbol('njak')
        Traceback (most recent call last):
        AssertionError
        >>> Simbol('zrak')
        ZRAK
        """
        assert name is not None
        uname = name.upper()
        assert uname not in Simbol.interned, uname
        self.name = uname
        Simbol.interned[self.name] = self

    @classmethod
    def get(cls, name):
        """
        >>> Simbol.get('foo')
        FOO
        >>> Simbol.get('bar') == Simbol.get('bar')
        True
        >>> Simbol.get('foo') != Simbol.get('bar')
        True
        """
        ret = Simbol.interned.get(name)
        return ret if ret is not None else Simbol(name)

    def __repr__(self):
        """
        >>> Simbol('lalala')
        LALALA
        """
        return self.name


Simbol.NIL = Simbol.get('NIL')
