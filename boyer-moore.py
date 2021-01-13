from naif import recherche_mot
import time


def pre_traitement(mot):
    """
    Calcule le dictionnaire des décalages pour un mot, en prétraitement de l'algo Boyer Moore
    :param mot: str
        Chaîne à traiter (mot à rechercher)
    :return: dict
        Dictionnaire contenant les décalages par lettre
    """
    decalages = {}
    n = len(mot)
    for i, lettre in enumerate(mot[:-1]):
        decalages[lettre] = n - i - 1
    return decalages


# Tests unitaires
assert pre_traitement("maman") == {'m': 2, 'a': 1}
assert pre_traitement("dab") == {'d': 2, 'a': 1}
assert pre_traitement("bonjour") == {'b': 6, 'o': 2, 'n': 4, 'j': 3, 'u': 1}
assert pre_traitement("algorithme") == {'a': 9, 'l': 8, 'g': 7, 'o': 6, 'r': 5, 'i': 4, 't': 3, 'h': 2, 'm': 1}


def boyer_moore(texte, mot):
    """
    Recherche d'un mot dans un texte par l'algorithme simplifié de Boyer Moore
    :param texte: str
        texte dans lequel rechercher le mot
    :param mot: str
        chaine à rechercher dans le texte
    :return: bool
        True si on a trouvé le mot dans le texte
    """
    decalages = pre_traitement(mot)
    n = len(mot)
    N = len(texte)

    i = n - 1
    while i < N:
        lettre = texte[i]
        if lettre == mot[-1]:
            # rechercher lettre par lettre
            k = 1
            trouve = True
            while trouve and k < n:
                if mot[-1-k] != texte[i-k]:
                    trouve = False
                k += 1
            if trouve:
                return True
        if lettre in decalages.keys():
            i += decalages[lettre]
        else:
            i += n
    return False


assert boyer_moore("abracadabra", "dab")
assert boyer_moore("abracadabra", "aba") is False
assert boyer_moore('abracadabra', 'obra') is False
assert boyer_moore('abracadabra', 'bara') is False
assert boyer_moore('maman est là', 'maman')
assert boyer_moore('bonjour maman', 'maman')
assert boyer_moore('bonjour maman', 'papa') is False


fichier = open("lerougeetlenoir.txt", "r")
roman = fichier.read()
fichier.close()

t1 = 0
d = time.time()
for i in range(100):
    boyer_moore(roman, "Julien trembla")
f = time.time()
t1 = t1 + f - d
print(t1)

t1 = 0
d = time.time()
for i in range(100):
    recherche_mot(roman, "Julien trembla")
f = time.time()
t1 = t1 + f - d
print(t1)
