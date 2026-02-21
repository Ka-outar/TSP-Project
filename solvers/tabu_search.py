import random
from solvers.hill_climbing import two_opt_swap

def tabu_search(instance, max_iter=500, tabu_size=15):
    """
    Algorithme de Recherche Tabou (Tabu Search) pour le TSP.
    """
    # 1. Initialisation : Générer un tour aléatoire
    current_tour = list(range(instance.n))
    random.shuffle(current_tour)
    current_dist = instance.total_distance(current_tour)
    
    best_tour = list(current_tour)
    best_dist = current_dist
    
    # Liste Tabou pour stocker les mouvements (indices inversés)
    tabu_list = []
    history = [best_dist]

    for _ in range(max_iter):
        neighborhood = []
        n = instance.n
        
        # 2. Générer un voisinage (explorer plusieurs voisins par 2-opt)
        for _ in range(20): # On teste 20 voisins aléatoires
            # On s'assure que i < j pour le 2-opt
            i, j = sorted(random.sample(range(n), 2))
            
            # Vérifier si le mouvement est dans la liste Tabou
            if (i, j) not in tabu_list:
                neighbor = two_opt_swap(current_tour, i, j)
                d = instance.total_distance(neighbor)
                neighborhood.append((neighbor, d, (i, j)))

        if not neighborhood:
            break

        # 3. Choisir le meilleur voisin (Aspiration : même s'il est moins bon que le courant)
        neighborhood.sort(key=lambda x: x[1])
        next_tour, next_dist, move = neighborhood[0]

        # 4. Mise à jour de la solution courante
        current_tour = next_tour
        current_dist = next_dist
        
        # Mise à jour du meilleur global
        if current_dist < best_dist:
            best_tour = list(current_tour)
            best_dist = current_dist

        # 5. Mise à jour de la liste Tabou (First-In, First-Out)
        tabu_list.append(move)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        history.append(best_dist)

    return best_tour, best_dist, history