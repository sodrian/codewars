def arithmetic(a, b, operator):
    dct = {
        'add': '+', 
        'subtract': '-',
        'multiply': '*',
        'divide': '/'}
    if operator in dct.keys():
        return eval('{} {} {}'.format(a, dct[operator], b))
    else:
        raise ValueError('Non valid operator {}'.format(operator))