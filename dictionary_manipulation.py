# Création d'un dictionnaire avec des clés entières
mon_dict = {1: "Pomme", 2: "Banane", 3: "Orange"}

# Affichage du dictionnaire initial
print("Dictionnaire initial :", mon_dict)

# Accéder à une valeur par sa clé
print("Valeur clé 1 :", mon_dict[1])

# Modifier une valeur existante
mon_dict[2] = "Mangue"
print("Après modification :", mon_dict)

# Ajouter une nouvelle clé
mon_dict[4] = "Citron"
print("Après ajout :", mon_dict)

# Supprimer une clé
del mon_dict[3]
print("Après suppression :", mon_dict)

# Utiliser get() pour accéder à une valeur
print("Valeur clé 3 :", mon_dict.get(3))  # Renvoie None

# Vérifier si une clé existe
print("Clé 2 existe :", 2 in mon_dict)

# Parcourir les clés
print("Clés :", list(mon_dict.keys()))

# Parcourir les valeurs
print("Valeurs :", list(mon_dict.values()))

# Parcourir les paires clé-valeur
for clé, valeur in mon_dict.items():
    print("Clé:", clé, "- Valeur:", valeur)

# Copier le dictionnaire
copie_dict = mon_dict.copy()
print("Copie :", copie_dict)

# Vider le dictionnaire
mon_dict.clear()
print("Dictionnaire après clear :", mon_dict)
