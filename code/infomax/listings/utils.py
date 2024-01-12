import random
import string

def generate_password(length):
    """ Retourne une chaine de caractère random de longueur 'length'.
      Utilisé généralement pour générer un mdp"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Example: Generate a random string of length 14
random_string = generate_password(14)
print(random_string)
