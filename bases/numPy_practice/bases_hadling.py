import numpy as np

# Créez un tableau 2D de shape (4,5) avec des valeurs aléatoires
random_arr = np.random.rand(4, 5)

# Affichez:
print("Shape:", random_arr.shape)  # Dimensions
print("Taille:", random_arr.size)  # Nombre total d'éléments
print("Type de données:", random_arr.dtype)  # Type des éléments
print("2ème ligne:", random_arr[1])  # Accès par index
print("Élément (2,3):", random_arr[2,3])  # Accès à un élément spécifique