def contar_caracteres(s):
    """Função que conta os caracteres de uma string

    >>> contar_caracteres('vasco')
    {'a': 1, 'c': 1, 'o': 1, 's': 1, 'v': 1}

    >>> contar_caracteres('eder')
    {'d': 1, 'e': 2, 'r': 1}

    :param s:  string a ser contada
    """
    resultado = {}
    for caracter in sorted(s):
        resultado[caracter] = resultado.get(caracter, 0) + 1
    return resultado

if __name__ == '__main__':
    print(contar_caracteres('vasco'))
    print(contar_caracteres('eder'))
    print(contar_caracteres('renzo'))


