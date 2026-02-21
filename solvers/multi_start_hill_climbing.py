from solvers.hill_climbing import hill_climbing_best
from solvers.hill_climbing_first import hill_climbing_first
def multi_start_hill_climbing(instance, n_starts=10, strategy="first"):
    """
    Multi-Start Hill Climbing.
    Lance l'algorithme de Hill Climbing plusieurs fois (n_starts) 
    depuis des solutions initiales aléatoires et garde le meilleur résultat global.
    """
    best_global_tour = None
    best_global_dist = float('inf')
    
    # Historique de la meilleure distance trouvée au fil des lancements
    global_history = [] 

    for start in range(n_starts):
        # On choisit quelle version du Hill Climbing on lance
        if strategy == "first":
            tour, dist, _ = hill_climbing_first(instance)
        else:
            tour, dist, _ = hill_climbing_best(instance)
        
        # Mise à jour si on a trouvé un meilleur optimum global
        if dist < best_global_dist:
            best_global_tour = tour
            best_global_dist = dist
            
        global_history.append(best_global_dist)
        
    return best_global_tour, best_global_dist, global_history