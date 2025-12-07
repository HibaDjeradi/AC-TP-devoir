import time
import sys
import os

# Changer le répertoire courant vers celui où se trouve le script. 
# Cela évite les erreurs "file not found" lorsque vous lisez ou écrivez des fichiers.
os.chdir(os.path.dirname(__file__))

#############################################################################################################################
# QUESTION 1 – Lecture du fichier
# Écrire une fonction Python permettant de lire les valeurs entières du fichier valeurs_aleatoires.txt
# La lecture doit se faire à l’aide d’une liste, en convertissant chaque ligne en entier.
#############################################################################################################################

def read_file(file_name):
    # Ouvre le fichier en mode lecture 'r'
    file = open(file_name, 'r')
    values = []   # Liste qui va contenir les entiers du fichier
    for line in file:
        # Convertir chaque ligne en entier et l'ajouter à la liste
        values.append(int(line.strip()))
    file.close()  # Fermer le fichier après lecture
    return values    

#############################################################################################################################
# QUESTION 2 – Comptage des occurrences (Complexité O(n²))
# Écrire une fonction nombre_occurrences(values_list) utilisant :
# - une boucle imbriquée
# - un dictionnaire pour stocker les occurrences
#
# QUESTION 3 – Analyse algorithmique
# - Indiquer le nombre exact d’itérations
# - Déterminer la complexité temporelle en notation O.
# - Intégrer un chronomètre pour mesurer la durée d’exécution
#############################################################################################################################

def nombre_occurrences(values_list):
    iterations = 0
    start_time = time.time()
    occurrences = dict()
    remaining_time = 0

    for i in range(n):
        iterations += 1
        count = 0
        for j in range(n):
            iterations += 1
            if values_list[j] == values_list[i]:
                count += 1
            occurrences[values_list[i]] = count
        
        #               100% --> n
        # elapsed_percentage --> i+1 => elapsed_percentage  = (i + 1) * 100 / n  
        elapsed_percentage   = (i + 1) * 100 / n
        remaining_percentage = 100 - elapsed_percentage 

        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_percentage  > 0:
            #    elapsed_time --> elapsed_percentage 
            #  remaining_time --> remaining_percentage => remaining_time = remaining_percentage * elapsed_time / elapsed_percentage 
            remaining_time = remaining_percentage * elapsed_time / elapsed_percentage 
        
        # Affiche la progression sur une seule ligne en écrasant l'affichage précédent.
        # \r ramène le curseur au début de la ligne, sys.stdout.write écrit le texte sans retour à la ligne,
        # et le formatage affiche le pourcentage, le temps écoulé et le temps restant estimé.
        sys.stdout.write(f"\rProgress: {elapsed_percentage :.2f}%, Elapsed Time: {elapsed_time:.2f}s, RemainingTime: {remaining_time:.2f}s")

        # Force l'affichage immédiat du texte (sinon Python peut attendre avant d'afficher).
        sys.stdout.flush()  

    end_time = time.time()
    print(f"\n⏱ Durée totale du comptage : {end_time - start_time:.5f} secondes")
    print(f"Nombre total d’itérations : {iterations}")
    return occurrences
# fin nombre_occurrences

#############################################################################################################################
# QUESTION 4 – Amélioration du calcul des occurrences (Complexité O(n))
# Écrire une fonction nombre_occurrences_ameliore(values_list)
# Objectif : réduire la complexité de O(n²) → O(n)
#############################################################################################################################

def nombre_occurrences_ameliore(values_list):
    iterations = 0
    start_time = time.time()
    occurrences = dict()

    for value in values_list:
        iterations += 1
        if value in occurrences:
            occurrences[value] += 1
        else:
            occurrences[value] = 1

        elapsed_percentage = iterations * 100 / len(values_list)
        elapsed_time = time.time() - start_time
        remaining_percentage = 100 - elapsed_percentage
        remaining_time = (remaining_percentage * elapsed_time / elapsed_percentage) if elapsed_percentage > 0 else 0

        sys.stdout.write(f"\rProgress: {elapsed_percentage:.2f}%, Elapsed Time: {elapsed_time:.2f}s, RemainingTime: {remaining_time:.2f}s")
        sys.stdout.flush()

    end_time = time.time()
    print(f"\n⏱ Durée totale du comptage optimisé : {end_time - start_time:.5f} secondes")
    print(f"Nombre total d’itérations : {iterations}")
    return occurrences



#############################################################################################################################
# QUESTION 5 – Tri par sélection (Selection Sort)
# Écrire une fonction selection_sort() qui :
# - trie les éléments en ordre croissant
# - indique le nombre exact d’itérations
# - affiche la complexité 
# - intègre un chronomètre
#############################################################################################################################

def selection_sort(lst):
    start = time.time()
    iteration = 0
    n = len(lst)
    
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            iteration += 1  # Count comparison
            if lst[j] < lst[min_index]:
                min_index = j
        # Swap if needed
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]
        elapsed_percentage = (i + 1) * 100 / n
        elapsed_time = time.time() - start
        remaining_percentage = 100 - elapsed_percentage
        remaining_time = (remaining_percentage * elapsed_time / elapsed_percentage) if elapsed_percentage > 0 else 0
        sys.stdout.write(f"\rProgress: {elapsed_percentage:.2f}%, Elapsed Time: {elapsed_time:.2f}s, RemainingTime: {remaining_time:.2f}s , RemainingDays: {second_todays(remaining_time)} days")
        sys.stdout.flush()
    elapsed = time.time() - start
    print("Complexité : O(n^2)")
    print(f"Nombre d'iterations: {iteration}")
    print(f"Le temps total pour le tri: {elapsed:.6f} seconds")
    return iteration, elapsed

def second_todays(seconds):
    day_s = 24*60*60
    remaining_days = seconds / day_s
    return remaining_days

#############################################################################################################################
# QUESTION 6 – Tri par fusion (Merge Sort)
# Écrire une fonction merge_sort(tab) qui :
# - trie les éléments en ordre croissant
# - compte le nombre d’itérations
# - affiche la complexité : O(n log n)
# - intègre un chronomètre
#############################################################################################################################

def merge_sort(lst):
    start_time = time.time()
    total_len = len(lst)  
    progress = 0          
    iteration = 0
    if len(lst) <= 1: 
        return 0
    
    halfLen = len(lst) // 2
    leftList = []
    rightList = []
    
    for i in range(len(lst)):
        iteration += 1
        if i < halfLen:
            leftList.append(lst[i])
        else:
            rightList.append(lst[i])

        progress += 1
        percent = progress * 100 / total_len
        elapsed = time.time() - start_time
        remaining = elapsed * (100 - percent) / percent if percent > 0 else 0

        sys.stdout.write(f"\rProgress: {percent:.2f}%, Elapsed: {elapsed:.2f}s, Remaining: {remaining:.2f}s")
        sys.stdout.flush()
        
    merge_count1 = merge_sort(leftList)
    merge_count2 = merge_sort(rightList)
    merge_count3 = merge(leftList, rightList, lst)
    iteration += merge_count1 + merge_count2 + merge_count3
    elapsed_t = time.time() - start_time
    print("Complexité O(n log n)")
    print(f"Nombre d'iterations: {iteration}")
    print(f"Le temps total pour le tri: {elapsed_t:.6f} seconds")
    return iteration


def merge(leftList, rightList, list):
    merge_count = 0
    leftLen = len(leftList) 
    rightLen = len(rightList)
    l = 0
    r = 0
    i = 0
    
    while l < leftLen and r < rightLen:
        merge_count += 1
        if leftList[l] < rightList[r]:
            list[i] = leftList[l]
            i += 1
            l += 1
        else: 
            list[i] = rightList[r]
            i += 1
            r += 1
    
    while l < leftLen:
        merge_count += 1
        list[i] = leftList[l]
        l += 1
        i += 1
        
    while r < rightLen:
        merge_count += 1
        list[i] = rightList[r]
        i += 1
        r += 1
     
    return merge_count


#############################################################################################################################
# QUESTION 7 – Sauvegarde du tableau trié
# Écrire une fonction write_to_file(tab) qui enregistre les valeurs triées dans 
# un fichier nommé valeurs_aleatoires_tries.txt
#############################################################################################################################

def write_to_file(tab, file_name="valeurs_aleatoires_tries.txt"):
    with open(file_name, 'w') as f:
        for value in tab:
            f.write(f"{value}\n")
    print(f"Les valeurs triées ont été sauvegardées dans '{file_name}'.")



#############################################################################################################################
# Début du script principal
#############################################################################################################################

# 1. Lecture du fichier
valeurs_aleatoires_list = read_file('valeurs_aleatoires.txt')
list_length = len(valeurs_aleatoires_list)
n = len(valeurs_aleatoires_list) # n est utilisé dans nombre_occurrences

print('Valeurs lues :', valeurs_aleatoires_list[:10], '...')
print('Longueur de la liste (n) :', n)

# 2. & 3. Comptage des occurrences (O(n²))
#occurrences_on2 = nombre_occurrences(valeurs_aleatoires_list)
# print("Occurrences (O(n²)) :", occurrences_on2)

# 4. Comptage des occurrences amélioré (O(n))
#occurrences_on = nombre_occurrences_ameliore(valeurs_aleatoires_list)
# print("Occurrences (O(n)) :", occurrences_on)

# 5. Tri par sélection (Selection Sort)
#values = valeurs_aleatoires_list.copy()  
#selection_sort(values)
#write_to_file(values)  

# 6. Tri par fusion (Merge Sort)
#values = valeurs_aleatoires_list.copy()  
#merge_sort(values)
#write_to_file(values)  

# 7. Sauvegarde du tableau trié
# write_to_file()





