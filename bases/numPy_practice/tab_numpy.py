import numpy as np

# tableau 1D

tab1D = np.array([1, 2, 3, 4, 5])
print("Tableau 1D:")
print(tab1D)


# tableau 2D
tab2D = np.array([[1, 2, 3], [4, 5, 6]])
print("\nTableau 2D:")
print(tab2D)

# tableau de b zéro
tab_zero = np.zeros((3, 4))  # 3 lignes, 4
print("\nTableau de zéros:")
print(tab_zero)

# tableau de b un
tab_one = np.ones((2, 3))  # 2 lignes, 3
print("\nTableau de uns:")
print(tab_one)

# Tableau avec places de valeur
tab_place = np.arange(0,10,2)  # de 0 à 10 avec un pas de 2
print("\nTableau avec des valeurs espacées:")
print(tab_place)

# Tableau avec des valeurs aléatoires
tab_random = np.random.rand(3, 3)  # 3 lignes,
# 3 colonnes avec des valeurs aléatoires entre 0 et 1
print("\nTableau avec des valeurs aléatoires:")
print(tab_random)


# Tableau identité 
tab_identity = np.eye(3)  # matrice identité de taille 3x3
print("\nTableau identité:")
print(tab_identity)