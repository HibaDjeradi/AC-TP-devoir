import os

# Changer le répertoire courant vers celui où se trouve le script. 
# Cela évite les erreurs "file not found" lorsque vous lisez ou écrivez des fichiers.
os.chdir(os.path.dirname(__file__))

def read_file(file_name):
    # Ouvre le fichier en mode lecture 'r'
    file = open(file_name, 'r')
    values = []   # Liste qui va contenir les entiers du fichier
    for line in file:
        # Convertir chaque ligne en entier et l'ajouter à la liste
        values.append(int(line.strip()))
    file.close()  # Fermer le fichier après lecture
    return values    

def write_to_file(file_name, values_list):
    # Ouvre le fichier en mode écriture 'w'
    file = open(file_name, 'w')
    for value in values_list:
        # Écrire chaque valeur dans le fichier, suivie d'un saut de ligne
        file.write(str(value) + '\n')
    file.close()  # Fermer le fichier après écriture

########################################################################################################################
# Debut du script principal pour tester les fonctions de lecture et d'écriture de fichiers 
 
# Liste de valeurs à écrire dans le fichier
data_to_write = [1, 10, -5, -3, 7, 0, 4, 2, 8, -2, 9, 6, -1, 5, -4, -6, 3]

# Écriture des valeurs dans le fichier numbers.txt
write_to_file('numbers.txt', data_to_write)

# Lecture des valeurs depuis le fichier
read_values = read_file('numbers.txt')

# Affichage du résultat
print(read_values)
# Fin du script principal

