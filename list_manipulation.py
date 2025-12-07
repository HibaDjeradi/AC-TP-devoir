# Création d'une liste
ma_liste = [10, 20, 30, 40]

# Affichage des éléments
print("Liste initiale :", ma_liste)

# Accès aux éléments
print("Premier élément :", ma_liste[0])
print("Dernier élément :", ma_liste[-1])

# Ajout d’un élément à la fin
ma_liste.append(50)
print("Après append(50) :", ma_liste)

# Insertion à une position donnée
ma_liste.insert(1, 15)
print("Après insert(1, 15) :", ma_liste)

# Suppression d’un élément par valeur
ma_liste.remove(20)
print("Après remove(20) :", ma_liste)

# Suppression du dernier élément
ma_liste.pop()
print("Après pop :", ma_liste)

# Vérifier la taille
print("Taille :", len(ma_liste))

# Tri de la liste
ma_liste.sort()
print("Liste triée :", ma_liste)

# Vérifier la présence d’un élément
print("30 est dans la liste :", 30 in ma_liste)
