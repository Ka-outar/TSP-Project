import random
from solvers.hill_climbing import two_opt_swap
def hill_climbing_first(instance):
    """
    Algorithme Hill Climbing avec stratégie First Improvement.
    On accepte la première solution voisine strictement meilleure.
    """
    # Génération d'une solution initiale aléatoire
    current_tour = list(range(instance.n))
    random.shuffle(current_tour)
    current_dist = instance.total_distance(current_tour)
    
    improved = True
    history = [current_dist]
    
    while improved:
        improved = False
        
        # Exploration des voisins (Voisinage 2-opt)
        for i in range(1, instance.n - 1):
            for k in range(i + 1, instance.n):
                neighbor = two_opt_swap(current_tour, i, k)
                neighbor_dist = instance.total_distance(neighbor)
                
                # Dès qu'une amélioration est trouvée, on l'accepte immédiatement
                if neighbor_dist < current_dist:
                    current_tour = neighbor
                    current_dist = neighbor_dist
                    history.append(current_dist)
                    improved = True
                    break # On casse la boucle 'k'
            
            if improved:
                break # On casse la boucle 'i' pour recommencer depuis le nouveau point
                
    return current_tour, current_dist, history