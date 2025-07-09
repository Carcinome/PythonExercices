from collections import Counter, defaultdict, namedtuple
from itertools import product, accumulate
import operator

"""
Importe les fonctions Counter et default_dict depuis le module collections
"""
fruits = ["pomme", "banane", "cerise"]
fruits.append("orange")
print(fruits[1])

mots = ["chat", "chien", "cheval", "tigre"]
longueurs = {mot: len(mot) for mot in mots}
print(longueurs)

premieres_lettres = {mot[0] for mot in mots}
print(premieres_lettres)

carres = [x**2 for x in range(10)]
print(carres)

def compte_jusque(n):
    for i in range(n):
        yield i

for nombre in compte_jusque(10):
    print(nombre)

compteur = Counter("abracadabra")
print(compteur)

liste_notes = ["Alice", "Bob", "Alice"]
notes = defaultdict(list)
for eleve in liste_notes:
    notes[eleve].append(20)
print(notes)

Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p.y)

for combinaison in product([1,2], ["a", "b"]):
    print(combinaison)

print(list(accumulate([1, 2, 3, 4], operator.mul)))


