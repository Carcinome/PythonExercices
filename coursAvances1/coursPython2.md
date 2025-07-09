🧩 Chapitre 2 : Structures de Données Avancées
Objectifs :

    Approfondir l’usage des types de collection en Python

    Comprendre les différences entre liste, tuple, dictionnaire, ensemble

    Introduire les compréhensions, les générateurs, et quelques modules standards

2.1. Listes

Les listes sont des collections ordonnées et modifiables.

fruits = ["pomme", "banane", "cerise"]
print(fruits[0])  # pomme
fruits.append("kiwi")  # Ajout
print(fruits)

⚠️ Points clés :

    L’indice commence à 0

    Une liste peut contenir n’importe quel type d’objet

    Elle est mutable : vous pouvez la modifier en place

🔧 Méthodes utiles :

liste = [1, 2, 3]
liste.append(4)
liste.remove(2)
liste.pop()       # Retire le dernier élément
liste.sort()      # Trie en place

🧠 Exercice 1 : Manipuler une liste

But : Gérer une liste de tâches.

taches = ["Lire", "Coder", "Dormir"]

    Ajoutez une tâche : "Manger"

    Supprimez "Dormir"

    Affichez la liste finale

Indice : utilisez .append() et .remove().

Correction :

taches = ["Lire", "Coder", "Dormir"]
taches.append("Manger")
taches.remove("Dormir")
print(taches)  # ['Lire', 'Coder', 'Manger']

2.2. Tuples

Les tuples sont ordonnés mais immuables.

coordonnees = (10, 20)
print(coordonnees[0])  # 10

    Ils sont utiles pour regrouper des données liées

    Leur immutabilité permet plus de sécurité

🧠 Exercice 2 : Tuple d’informations

Crée un tuple utilisateur contenant :

    le nom "Alice"

    l’âge 30

Puis affiche le nom.

Indice : utilisez print(utilisateur[0]).

Correction :

utilisateur = ("Alice", 30)
print(utilisateur[0])  # Alice

2.3. Dictionnaires

Les dictionnaires associent des clés à des valeurs.

personne = {"nom": "Alice", "age": 30}
print(personne["nom"])  # Alice

🔧 Méthodes utiles :

personne["ville"] = "Paris"   # Ajout
del personne["age"]           # Suppression
print(personne.keys())        # Clés
print(personne.values())      # Valeurs

🧠 Exercice 3 : Dictionnaire de profil

Créer un dictionnaire avec les clés : "nom", "âge", "email". Puis afficher l’e-mail.

Correction :

profil = {
    "nom": "Alice",
    "âge": 30,
    "email": "alice@example.com"
}
print(profil["email"])

2.4. Ensembles (sets)

Un ensemble est une collection non ordonnée et sans doublons.

notes = {10, 12, 14, 14, 10}
print(notes)  # {10, 12, 14}

Utile pour :

    Éliminer les doublons

    Effectuer des opérations ensemblistes

🔧 Opérations ensemblistes :

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union : {1, 2, 3, 4, 5}
print(a & b)  # Intersection : {3}
print(a - b)  # Différence : {1, 2}

🧠 Exercice 4 : Nettoyer une liste

Retirez les doublons de la liste suivante :

nombres = [1, 2, 2, 3, 4, 4, 5]

Indice : convertissez en set, puis retransformez en list.

Correction :

nombres = [1, 2, 2, 3, 4, 4, 5]
uniques = list(set(nombres))
print(uniques)  # [1, 2, 3, 4, 5]

2.5. Compréhensions

Les compréhensions permettent d’écrire du code plus concis.

cubes = [x**3 for x in range(5)]
print(cubes)  # [0, 1, 8, 27, 64]

⚠️ Ne pas abuser de la concision au détriment de la lisibilité.
🧠 Exercice 5 : Liste des carrés pairs

Crée une liste contenant les carrés des nombres pairs de 0 à 10.

Indice : Utilisez [x**2 for x in range(11) if x % 2 == 0].

Correction :

carres_pairs = [x**2 for x in range(11) if x % 2 == 0]
print(carres_pairs)  # [0, 4, 16, 36, 64, 100]

2.6. Générateurs

Les générateurs produisent des valeurs à la demande, sans tout garder en mémoire.

def compte():
    for i in range(5):
        yield i

for nombre in compte():
    print(nombre)

Avantages :

    Plus efficace pour les grandes quantités de données

    Ne consomme de mémoire que pour l’élément courant

2.7. Le module collections

Python propose des types spécialisés :

    Counter : compte les éléments

    defaultdict : dictionnaire avec valeur par défaut

    deque : file double (pile/queue optimisée)

Exemple :

from collections import Counter
lettres = Counter("abracadabra")
print(lettres)  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

2.8. Le module itertools

Permet de manipuler des itérateurs puissants :

from itertools import accumulate

nombres = [1, 2, 3, 4]
print(list(accumulate(nombres)))  # [1, 3, 6, 10]

🎯 Projet de fond : Gestionnaire de tâches (partie 2)

Nous allons maintenant stocker les tâches dans une structure plus robuste.

taches = [
    {"titre": "Lire", "fait": False},
    {"titre": "Coder", "fait": True},
]

Affiche chaque tâche avec son statut :

for t in taches:
    etat = "✓" if t["fait"] else "✗"
    print(f"{etat} {t['titre']}")

Prochaine étape :

→ On apprendra à ajouter, marquer comme faite, et supprimer une tâche dans le prochain chapitre.
