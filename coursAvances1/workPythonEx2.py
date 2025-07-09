"""
Exercice de manipulation de liste.
"""

taches = ["Lire", "Coder", "Dormir"]
print(taches)

taches.append("Manger")
taches.remove("Dormir")
print(taches)

"""
Exercice de manipulation de tuple.
"""

utilisateur = ("Alice", 30)
print(utilisateur[0])

"""
Exercice de manipulation de dictionnaire.
"""

profil = {
    "nom": "Alice",
    "âge": 32,
    "email" : "alice@email.com"
}

print(profil["email"])


"""
Exercice de manipulation d'ensembles.
"""

nombres = [1, 2, 2, 3, 4, 4, 5]
uniques = list(set(nombres))
print(uniques)

"""
Exercice de manipulation de compréhensions.
"""

carres_pairs = [x**2 for x in range(11) if x % 2 == 0]
print(carres_pairs)


