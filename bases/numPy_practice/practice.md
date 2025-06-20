# Guide Pratique de NumPy : Manipulation de Tableaux

NumPy (Numerical Python) est une bibliothèque fondamentale pour le calcul scientifique en Python. Elle fournit des objets tableau multidimensionnels de haute performance et des outils pour travailler avec ces tableaux.

## 1. Installation de NumPy

Avant de commencer, assurez-vous d'avoir NumPy installé :

```bash
pip install numpy
```

## 2. Importation de NumPy

La convention standard est d'importer NumPy comme suit :

```python
import numpy as np
```

## 3. Création de Tableaux NumPy

### Tableau à partir d'une liste Python

```python
# Tableau 1D
arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d)

# Tableau 2D
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
```

### Tableaux spéciaux

```python
# Tableau de zéros
zeros = np.zeros((3, 4))  # 3 lignes, 4 colonnes

# Tableau de uns
ones = np.ones((2, 3))

# Tableau identité
identity = np.eye(3)  # Matrice 3x3

# Tableau avec plage de valeurs
range_arr = np.arange(0, 10, 2)  # De 0 à 10 (exclu) par pas de 2

# Tableau avec valeurs espacées linéairement
linspace_arr = np.linspace(0, 1, 5)  # 5 valeurs entre 0 et 1
```

## 4. Travaux Pratiques : Manipulation de Base

### TP 1: Exploration des tableaux

```python
# Créez un tableau 2D de shape (4,5) avec des valeurs aléatoires
random_arr = np.random.rand(4, 5)

# Affichez:
print("Shape:", random_arr.shape)  # Dimensions
print("Taille:", random_arr.size)  # Nombre total d'éléments
print("Type de données:", random_arr.dtype)  # Type des éléments
print("2ème ligne:", random_arr[1])  # Accès par index
print("Élément (2,3):", random_arr[2, 3])  # Accès à un élément spécifique
```

### TP 2: Opérations mathématiques

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Opérations élément par élément
print("Addition:", a + b)
print("Multiplication:", a * b)
print("Exponentiation:", a ** 2)

# Fonctions mathématiques
print("Sinus:", np.sin(a))
print("Logarithme:", np.log(a))
print("Somme:", np.sum(a))
print("Moyenne:", np.mean(a))
```

### TP 3: Indexation et Slicing avancé

```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Slicing
print("Deux premières lignes:\n", arr[:2])
print("Dernière colonne:\n", arr[:, -1])

# Indexation booléenne
mask = arr > 5
print("Masque booléen:\n", mask)
print("Valeurs > 5:\n", arr[mask])

# Indexation avec liste
print("Lignes 0 et 2:\n", arr[[0, 2]])
```

## 5. Manipulation de Shape et Redimensionnement

### TP 4: Changement de forme

```python
arr = np.arange(12)

# Redimensionner
reshaped = arr.reshape(3, 4)
print("Redimensionné 3x4:\n", reshaped)

# Aplatir
flattened = reshaped.flatten()
print("Aplati:\n", flattened)

# Transposition
transposed = reshaped.T
print("Transposé:\n", transposed)
```

## 6. Algèbre Linéaire avec NumPy

### TP 5: Opérations matricielles

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Produit matriciel
dot_product = np.dot(a, b)
print("Produit matriciel:\n", dot_product)

# Déterminant
det = np.linalg.det(a)
print("Déterminant de a:", det)

# Inverse
inv = np.linalg.inv(a)
print("Inverse de a:\n", inv)

# Valeurs propres
eigenvals = np.linalg.eig(a)
print("Valeurs propres de a:", eigenvals)
```

## 7. Traitement d'Images avec NumPy (Bonus)

Les images peuvent être représentées comme des tableaux NumPy :

```python
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

# Charger une image
img = mpimg.imread('image.jpg')  # Remplacez par un chemin valide
print("Shape de l'image:", img.shape)  # (hauteur, largeur, canaux)

# Convertir en niveaux de gris
gray = np.mean(img, axis=2)
plt.imshow(gray, cmap='gray')
plt.show()

# Rogner l'image
cropped = img[50:200, 100:300]
plt.imshow(cropped)
plt.show()
```

## 8. Exercices Pratiques

1. Créez une matrice 5x5 avec des 1 sur les bords et 0 à l'intérieur
2. Normalisez un tableau aléatoire 10x10 pour que ses valeurs soient entre 0 et 1
3. Calculez la moyenne de chaque colonne d'un tableau 2D
4. Trouvez l'index de la valeur maximale dans chaque ligne d'un tableau
5. Créez un damier 8x8 (alternance de 0 et 1)

### Solutions

```python
# 1. Matrice bordée
border = np.ones((5,5))
border[1:-1, 1:-1] = 0

# 2. Normalisation
rand_arr = np.random.random((10,10))
normalized = (rand_arr - rand_arr.min()) / (rand_arr.max() - rand_arr.min())

# 3. Moyenne par colonne
arr = np.random.rand(5, 3)
col_means = arr.mean(axis=0)

# 4. Index des maxima par ligne
max_indices = arr.argmax(axis=1)

# 5. Damier
checkerboard = np.zeros((8,8))
checkerboard[::2, ::2] = 1
checkerboard[1::2, 1::2] = 1
```

NumPy est une bibliothèque puissante qui forme la base de nombreux autres outils scientifiques en Python comme Pandas, SciPy et scikit-learn. Maîtriser NumPy est essentiel pour toute personne travaillant dans le domaine de la science des données ou du calcul numérique.