from symbol2 import Symbol


def eval2(data):
    """

    """
    if data == Symbol.NIL or data == Symbol.get('T'):
        return data
    raise ValueError(f'The variable {data} is unbound.')
