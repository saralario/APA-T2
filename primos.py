"""
Sara Lario Garrido

Tests unitaris requerits per validar les funcions:

>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcm(42, 60, 70, 63)
1260

>>> mcd(840, 630, 1050, 1470)
210
"""

def esPrimo(numero):
    """
    Determina si un número és primer. Retorna True si és primer, False si no ho és.
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("L'argument ha de ser un número natural major que 1.")
    
    # Comprovació d'eficiència 
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def primos(numero):
    """
    Retorna una tupla amb tots els números primers menors que l'argument.
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))


def descompon(numero):
    """
    Retorna una tupla amb la descomposició en factors primers de l'argument.
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("L'argument ha de ser un número natural major que 1.")
    
    factors = []
    divisor = 2
    temp = numero
    while divisor * divisor <= temp:
        while temp % divisor == 0:
            factors.append(divisor)
            temp //= divisor
        divisor += 1
    if temp > 1:
        factors.append(temp)
    return tuple(factors)


def mcd(*numeros):
    """
    Calcula el màxim comú divisor d'un nombre arbitrari d'arguments
    a partir de la seva descomposició factorial.
    """
    if not numeros:
        return None
    
    llista_freqs = []
    for n in numeros:
        factors = descompon(n)
        d = {}
        for f in factors:
            d[f] = d.get(f, 0) + 1
        llista_freqs.append(d)
    
    factors_comuns = set(llista_freqs[0].keys())
    for d in llista_freqs[1:]:
        factors_comuns &= set(d.keys())
    
    resultat = 1
    for f in factors_comuns:
        exp_minim = min(d[f] for d in llista_freqs)
        resultat *= (f ** exp_minim)
    
    return resultat


def mcm(*numeros):
    """
    Calcula el mínim comú múltiple d'un nombre arbitrari d'arguments
    a partir de la seva descomposició factorial.
    """
    if not numeros:
        return None
    
    max_exponents = {}
    
    for n in numeros:
        factors = descompon(n)
        actual_freqs = {}
        for f in factors:
            actual_freqs[f] = actual_freqs.get(f, 0) + 1
        
        for f, exp in actual_freqs.items():
            if f not in max_exponents or exp > max_exponents[f]:
                max_exponents[f] = exp
    
    resultat = 1
    for f, exp in max_exponents.items():
        resultat *= (f ** exp)
    
    return resultat


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)