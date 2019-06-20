def contar_caracteres(s):
    """Função que conta os caracteres de uma string

    >>> contar_caracteres('vasco')
    a: 1
    c: 1
    o: 1
    s: 1
    v: 1

    >>> contar_caracteres('eder')
    d: 1
    e: 2
    r: 1

    :param s:  string a ser contada
    """

    s_ordenado = sorted(s)# sorted ordena qualquer iterário
    anterior = s_ordenado[0]
    contagem = 1
    for caracter in s_ordenado[1:]:
        if(caracter == anterior):
            contagem += 1
        else:
            print(f'{anterior}: {contagem}')
            anterior = caracter
            contagem = 1
    print(f'{anterior}: {contagem}')

if __name__ == '__main__':
    print(contar_caracteres('vasco'))
    print(contar_caracteres('eder'))


