T = [0] * 10 
max = 0 

print("Entrez le premier entier : ")
T[0] = int(input())
max = T[0]

for i in range(1, 10):
    T[i] = int(input(f"Entrez l'entier pour la position {i + 1} : "))
    
    if T[i] > max:
        max_value = T[i]

print("Le maximum des éléments du tableau est :", max)
