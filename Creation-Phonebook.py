### Création d'un repertoire téléphonique

### Menu:
def Menu_Rep():
    # Options:
    Q = "0-Quitter"
    E = "1-Ecrire dans le repertoire"
    R = "2-Recherche dans le repertoire"
    C = "Votre choix ?"
    ### Affichage:
    print(f"{Q} \n{E}\n{R}\n\n{C}\n")

    return

### Ecrire
def Ecrire_Rep():
    # Saisir le nom du contact à enregistrer
    Name=input('Nom (0 pour Quitter): ')
    # Saisie de 0 --> retour au Menu principal
    if Name == str (0):
        Menu_Rep()
    else:
        # Saisir le numéro de téléphone pour le contact à enregistrer
        Num=input('Num Téléphone: ')
        Contact = Name + '  ' + Num
        # Créer le repertoire et enregistrer le contact
        with open('Repertoire.txt','a') as f :
            f.write(Contact)

        Ecrire_Rep()

    return

### Chercher
def Chercher_Rep():
    # Saisir le nom à rechercher
    Name=input('Entrer un nom: ')
    # Parcourir les contacts du repertoire
    with open('Repertoire.txt','r') as f:
        lignes = f.readlines()
        for ligne in lignes:
            # Si le nom existe dans les lignes
            if Name in ligne:
                Contact = ligne.split()
                # Récupérer le numéro de téléphone (Position 2 --> Indice 1)
                Contact = f"Le numéro recherché est: {Contact[1]}"
                break
            else:
                # Nom introuvable dans les lignes (Contact inconnu)
                Contact = f"Le contact recherché pour '{Name}' est inconnu"
    print(Contact)

    return

### Boite de dialogue:
# Affichage du Menu principal
Menu_Rep()
# Saisir pour choisir
Ch =input('Choix = ')
NumChoix = int (Ch)
# Affichage selon le choix
match NumChoix:
    case 0:
        Menu_Rep()
    case 1:
        Ecrire_Rep()
    case 2:
        Chercher_Rep()
