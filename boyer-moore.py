def pre_traitement(mot):
    decalages = {}
    n = len(mot)
    for i, lettre in enumerate(mot[:-1]):
        decalages[lettre] = n - i - 1
    return decalages


assert pre_traitement("maman") == {'m': 2, 'a': 1}
assert pre_traitement("dab") == {'d': 2, 'a': 1}
assert pre_traitement("bonjour") == {'b': 6, 'o': 2, 'n': 4, 'j': 3, 'u': 1}
