"""
Exercice de manipulation des générateurs.
"""

"""def nombres_pairs():
    for i in range(12):
        if i % 2 == 0:
            yield i
for nombre in nombres_pairs():
    print(nombre)


def compte():
    for i in range(5):
        yield i
for nombre in compte():
    print(nombre)


def lettres():
    yield "a"
    yield "b"
    yield "c"
for l in lettres():
    print(l)

def lettres():
    for i in range(ord("a"), ord("z") + 1):
        yield chr(i)
for l in lettres():
    print(l, end=" ")

def voyelles():
    voyelles_set = "aeiouyAEIOUY"
    for i in range(ord("a"), ord("z") + 1):
        lettre = chr(i)
        if lettre in voyelles_set:
            yield lettre
    for i in range(ord("A"), ord("Z") + 1):
        lettre = chr(i)
        if lettre in voyelles_set:
            yield lettre
for l in voyelles():
    print(l, end=" ")

def boucle_lettres():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while True:
        for lettre in alphabet:
            yield lettre
gen = boucle_lettres()
for _ in range(30):
    print(next(gen), end=" ")

def voyelles_infinies():
    voyelles_set = "aeiouy"
    while True:
        for lettre in voyelles_set:
            yield lettre
for l in voyelles_infinies():
    print(l, end=" ")"""

def lettres_a_z(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while True:
        for lettre in alphabet:
            yield lettre
for l in lettres_a_z(10):
    print(l, end=" ")
