class File:
    """Fichier."""
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        """Affiche le fichier."""
        print(f"Fichier '{self.name}")
    
class ImageFile(File):
    """Fichier image.
Rien de plus pour l'instant."""
    pass

class User:
    """Utilisateur."""
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        """Connecte l'utilisateur."""
        print(f"L'utilisateur {self.username} est connecté.")

    def post(self, thread, content, file=None):
        """Poste un message dans un fil de discussion."""
        if file: 
            post = FilePost(self, "aujourd'hui", content, file)
        else:
            post = Post(user=self, time_posted ="aujourd'hui", content=content)
        thread.add_post(post)
        return post

    def make_thread(self, title, content):
        """Crée un nouveau fil de discussion."""
        post = Post(self, "aujourd'hui", content)
        return Thread(title, "aujourd'hui", post)

    def __str__(self):
        """Représentation de l'utilisateur."""
        return self.username
    
class Moderator(User):
    """Utilisateur modérateur"""

    def edit(self, post, content):
        """Modifie un message."""
    
    def delete(self, thread,post):
        """Supprime un message."""
        index = thread.posts.index(post)
        del thread.posts[index]


class Post:
    """Message."""

    def __init__(self, user, time_posted, content):
        """Initialise l'utilisateur, la date et le contenu."""
        self.user = user
        self.time_posted = time_posted
        self.content = content
    
    def display(self):
        """Affiche le message."""
        print(f"Message posté par {self.user} le {self.time_posted}:")
        print({self.content})


class FilePost(Post):

    def __init__(self, user, time_posted, content, file):
        """Initialise le fichier."""
        super().__init__(user, time_posted, content)
        self.user = user
        self.time_posted = time_posted
        self.content = content
        self.file = file
    
    def display(self):
        """Affiche le contenu du fichier."""
        super().display()
        print("Pièce jointe:")
        self.file.display()

class Thread:
    """Fil de discussions."""

    def __init__(self, title, time_posted, post):
        """Initialise le titre, la date et les posts."""
        self.title = title
        self.time_posted = time_posted
        self.post = [post]

    def display(self):
        """Affiche le fil de discussion."""
        print("-------- THREAD --------")
        print(f"Titre: {self.title}, date: {self.time_posted}")
        print()
        for post in self.post:
            post.display()
            print()
            print("----------------")

    def add_post(self, post):
        """Ajoute un post."""
        self.post.append(post)
