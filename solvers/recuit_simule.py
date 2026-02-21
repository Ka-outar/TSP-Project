import numpy as np
import random
import math

def simulated_annealing(instance, T0=100.0, alpha=0.995, max_iter=5000):
    """
    Implémentation de l'algorithme du Recuit Simulé pour le TSP.
    """
    # 1. Solution initiale aléatoire
    current_tour = list(range(instance.n))
    random.shuffle(current_tour)
    current_dist = instance.total_distance(current_tour)
    
    best_tour = list(current_tour)
    best_dist = current_dist
    
    T = T0
    history = [current_dist]
    
    # 2. Boucle principale
    for _ in range(max_iter):
        # Générer un voisin avec l'opérateur 2-opt
        i, k = sorted(random.sample(range(instance.n), 2))
        # Inversion du segment entre i et k
        neighbor = current_tour[0:i] + current_tour[i:k+1][::-1] + current_tour[k+1:]
        neighbor_dist = instance.total_distance(neighbor)
        
        delta = neighbor_dist - current_dist
        
        # 3. Critère de Metropolis
        if delta < 0 or random.random() < math.exp(-delta / T):
            current_tour = neighbor
            current_dist = neighbor_dist
            
            # Sauvegarder la meilleure solution trouvée globalement
            if current_dist < best_dist:
                best_tour = list(current_tour)
                best_dist = current_dist
        
        # 4. Refroidissement de la température
        T *= alpha
        history.append(best_dist)
        
    return best_tour, best_dist, history