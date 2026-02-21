import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt

# S'assurer que les dossiers locaux sont reconnus
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.tsp_model import TSPInstance
from solvers.hill_climbing import hill_climbing_best
from solvers.hill_climbing_first import hill_climbing_first
from solvers.multi_start_hill_climbing import multi_start_hill_climbing
from solvers.recuit_simule import simulated_annealing
from solvers.tabu_search import tabu_search

# 1. Préparation des instances
def get_instances():
    np.random.seed(42) # Seed fixe pour la reproductibilité
    return {
        "Instance A (20 villes)": TSPInstance(np.random.rand(20, 2) * 100),
        "Instance B (50 villes)": TSPInstance(np.random.rand(50, 2) * 100),
    }

# Dictionnaire des algorithmes à tester
def get_algorithms():
    return {
        "HC (Best Imp.) ": lambda inst: hill_climbing_best(inst),
        "HC (First Imp.)": lambda inst: hill_climbing_first(inst),
        "Multi-Start HC ": lambda inst: multi_start_hill_climbing(inst, n_starts=10, strategy="first"),
        "Recuit Simulé  ": lambda inst: simulated_annealing(inst, T0=200, alpha=0.995, max_iter=5000),
        "Recherche Tabou": lambda inst: tabu_search(inst, max_iter=1000, tabu_size=20)
    }

# 2. Partie Statistique (30 Runs sur les instances) - Pour le tableau du rapport
def run_experiments(n_runs=30):
    instances = get_instances()
    algos = get_algorithms()
    
    print("=========================================================")
    print(f"🌍 Lancement de la campagne : {n_runs} Runs par algorithme")
    print("=========================================================\n")

    for inst_name, instance in instances.items():
        print(f"📍 {inst_name.upper()}")
        print("-" * 65)
        
        for algo_name, algo_func in algos.items():
            costs = []
            times = []
            
            for _ in range(n_runs):
                start_t = time.time()
                _, dist, _ = algo_func(instance)
                end_t = time.time()
                
                costs.append(dist)
                times.append(end_t - start_t)
            
            # Affichage formaté pour faciliter la copie dans ton rapport
            print(f"| {algo_name} | Min: {np.min(costs):7.2f} | Moy: {np.mean(costs):7.2f} | Std: {np.std(costs):6.2f} | Tps(s): {np.mean(times):6.4f} |")
        print("=" * 65 + "\n")

# 3. Partie Visualisation (Pour TOUTES les instances)
def show_visuals():
    print("📈 Génération des graphiques de convergence et de la Map pour toutes les instances...")
    
    instances = get_instances()
    
    # On boucle sur chaque instance pour générer ses graphiques
    for inst_name, instance in instances.items():
        print(f"⏳ Calculs en cours pour l'affichage de : {inst_name}...")
        
        # Exécution pour capturer l'historique de chaque algo
        _, _, hc_best_hist = hill_climbing_best(instance)
        _, _, hc_first_hist = hill_climbing_first(instance)
        _, _, mshc_hist = multi_start_hill_climbing(instance, n_starts=10)
        sa_tour, sa_dist, sa_hist = simulated_annealing(instance, T0=200, alpha=0.995, max_iter=8000)
        _, _, tabu_hist = tabu_search(instance, max_iter=1500, tabu_size=20)

        # --- Création d'une nouvelle fenêtre par instance ---
        plt.figure(figsize=(14, 5))
        plt.suptitle(f"Analyse Visuelle : {inst_name}", fontsize=14, fontweight='bold')
        
        # --- Graphique de Convergence ---
        plt.subplot(1, 2, 1)
        plt.plot(hc_best_hist, label="HC (Best)", color='red')
        plt.plot(hc_first_hist, label="HC (First)", color='orange')
        plt.plot(mshc_hist, label="Multi-Start HC", color='green')
        plt.plot(sa_hist, label="Recuit Simulé", color='blue')
        plt.plot(tabu_hist, label="Recherche Tabou", color='purple')
        
        plt.title("Convergence des algorithmes")
        plt.xlabel("Itérations / Mouvements acceptés")
        plt.ylabel("Distance")
        plt.legend()
        plt.grid(True)

        # --- Graphique de la Map (Chemin du Recuit Simulé) ---
        plt.subplot(1, 2, 2)
        # On ajoute la première ville à la fin pour fermer la boucle
        sa_tour_plot = list(sa_tour) + [sa_tour[0]]
        coords = instance.coords
        coords_plot = coords[sa_tour_plot]
        
        plt.plot(coords_plot[:, 0], coords_plot[:, 1], 'bo-', mfc='red', markersize=5)
        
        # Ajout du numéro des villes sur le graphe (optionnel mais très pratique)
        for idx, (x, y) in enumerate(coords):
            plt.text(x, y+1.5, str(idx), fontsize=8, color='darkred')
            
        plt.title(f"Meilleur trajet trouvé par le Recuit Simulé (Distance: {sa_dist:.2f})")
        
        plt.tight_layout()
        plt.subplots_adjust(top=0.88) # Ajustement pour le Suptitle

    # Afficher toutes les fenêtres créées à la fin
    plt.show()

if __name__ == "__main__":
    # 1. Lance les statistiques
    run_experiments(n_runs=30)
    
    # 2. Affiche les graphiques
    show_visuals()