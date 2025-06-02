import hashlib

def cryptage_md5(message):
    message_bytes=message.encode()
    hash_md5=hashlib.md5()
    hash_md5.update(message_bytes)
    hash_hex=hash_md5.hexdigest()
    return hash_hex

def bruteforce(message):
    # Fusionner les deux listes en une seule
    elements=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# Liste pour stocker toutes les combinaisons générées
    combinaisons=[]
    # Pour chaque longueur de combinaison (de 1 à 6)
    for longueur in range(1, 7):
        # Initialiser une pile pour simuler la récursion
        # Chaque élément de la pile sera une liste représentant une combinaison en cours
        pile=[]
        # On commence par mettre chaque élément de base dans la pile comme point de départ
        for e in elements:
            pile.append([e])
        # Boucle pour traiter les éléments de la pile
        while pile:
            # Extraire une combinaison partielle de la pile
            courant=pile.pop()
            # Si elle est de la longueur voulue, on l'ajoute à la liste finale
            if len(courant)==longueur:
                combinaison=''.join(courant)
                combinaisons.append(combinaison)
            else:
                # Sinon, on la prolonge avec tous les éléments possibles et on les remet dans la pile
                for e in elements:
                    nouvelle_combinaison=courant + [e]
                    pile.append(nouvelle_combinaison)
            # Si la combinaison est la bonne est alors le programme s'arrete et l'on renvoie le message 
            # qui est la combinaison
            if cryptage_md5(combinaisons)==message:
                return combinaisons



message=input()
message=cryptage_md5(message)
print(message)
print(bruteforce(message))
