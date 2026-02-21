import random

def two_opt_swap(tour, i, k):
    """Effectue une inversion 2-opt entre les indices i et k."""
    return tour[0:i] + tour[i:k+1][::-1] + tour[k+1:]

def hill_climbing_best(instance):
    """Algorithme Hill Climbing avec stratégie Best Improvement."""
    # Génération d'une solution initiale aléatoire
    current_tour = list(range(instance.n))
    random.shuffle(current_tour)
    current_dist = instance.total_distance(current_tour)
    
    improved = True
    history = [current_dist]
    
    while improved:
        improved = False
        best_neighbor = current_tour
        best_neighbor_dist = current_dist
        
        # Exploration de tous les voisins possibles (Voisinage 2-opt)
        for i in range(1, instance.n - 1):
            for k in range(i + 1, instance.n):
                neighbor = two_opt_swap(current_tour, i, k)
                neighbor_dist = instance.total_distance(neighbor)
                
                if neighbor_dist < best_neighbor_dist:
                    best_neighbor = neighbor
                    best_neighbor_dist = neighbor_dist
                    improved = True
        
        # Si on a trouvé un meilleur voisin, on met à jour
        if improved:
            current_tour = best_neighbor
            current_dist = best_neighbor_dist
            history.append(current_dist)
            
    return current_tour, current_dist, history