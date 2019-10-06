from simbol import Simbol


class Read():
    def __call__(self, data):
        """
        >>> Read()('()')
        NIL
        >>> Read()('NIL')
        NIL
        >>> Read()('T')
        T
        >>> Read()('t')
        T
        """
        if data == 'T':
            return Simbol.get('T')
        if data in ['()', 'NIL']:
            return Simbol.NIL
        return Simbol.get(data)
