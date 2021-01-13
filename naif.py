def recherche_mot(texte, mot):
    """
    Recherche un mot dans un texte
    :param texte: str
        le texte dans lequel on effectue la recherche
    :param mot: str
        le mot recherché
    :return: bool
        renvoie True si on a trouvé le mot
    """
    N = len(texte)
    n = len(mot)
    for i in range(N - n + 1):
        recherche = True
        k = 0
        while recherche and k < n:
            if mot[k] != texte[i + k]:
                recherche = False
            k = k + 1
        if recherche:
            return True
    return False


assert recherche_mot("abracadabra", "dab")
assert recherche_mot("abracadabra", "aba") is False
assert recherche_mot('abracadabra', 'obra') is False
assert recherche_mot('abracadabra', 'bara') is False
assert recherche_mot('maman est là', 'maman')
assert recherche_mot('bonjour maman', 'maman')
assert recherche_mot('bonjour maman', 'papa') is False
