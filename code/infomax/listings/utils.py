import random
import string

def generate_password(length):
    """ Retourne une chaine de caractère random de longueur 'length'.
      Utilisé généralement pour générer un mdp
      Return : String
      """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

