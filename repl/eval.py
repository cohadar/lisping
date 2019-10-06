from simbol import Simbol


class Eval():
    def __call__(self, data):
        """
        """
        if data == Simbol.NIL or data == Simbol.get('T'):
            return data
        raise ValueError(f'The variable {data} is unbound.')
