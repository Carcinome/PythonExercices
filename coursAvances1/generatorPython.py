"""
Exercice de manipulation des générateurs.
"""

def nombres_pairs():
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
