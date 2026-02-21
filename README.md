# 🌍 Projet M1 : Comparaison de Métaheuristiques pour le TSP

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Numpy](https://img.shields.io/badge/Numpy-Compat-orange?style=for-the-badge&logo=numpy)
![Status](https://img.shields.io/badge/Status-Terminé-success?style=for-the-badge)

> **Université Hassan II de Casablanca - ENSET Mohammedia** > **Master :** SDIA (Sciences des Données et Intelligence Artificielle)  
> **Module :** Optimisation & Métaheuristiques  
> **Encadrant :** Prof. MESTARI  

### 👥 Réalisé par :
* **Essayouti Atiqa**
* **Timourti Sana**
* **Misbah Kaoutar**

---

## 📝 Description du Projet

Ce projet vise à résoudre le célèbre **Problème du Voyageur de Commerce (TSP)** en comparant deux approches d'optimisation basées sur l'opérateur de voisinage **2-opt** :
1. **🏔️ Hill Climbing (Best Improvement)** : Recherche locale intensive pour trouver l'optimum le plus proche.
2. **🔥 Recuit Simulé (Simulated Annealing)** : Métaheuristique stochastique utilisant le critère de Metropolis pour s'échapper des optima locaux.

---

## 📂 Architecture du Code
Le projet est structuré de manière modulaire pour garantir la réutilisation des composants :
* `core/` : Gestion de l'instance TSP et calcul des distances.
* `solvers/` : Implémentation des algorithmes (HC et SA).
* `main.py` : Pilotage des tests statistiques et visualisation.



---

## 📊 Résultats Statistiques (30 Runs - 50 Villes)

Pour une analyse rigoureuse, les résultats suivants sont basés sur la moyenne de 30 exécutions indépendantes :

| Algorithme | Meilleur Coût 🏆 | Moyenne (Mean) | Écart-type (Std) |
| :--- | :--- | :--- | :--- |
| **Hill Climbing** | **567.15** | **590.95** | **16.09** |
| **Recuit Simulé** | 582.55 | 619.51 | 27.06 |

> **Analyse :** Le **Hill Climbing** montre une excellente stabilité et rapidité sur cette instance. Le **Recuit Simulé**, bien que puissant, nécessite un réglage fin de son schéma de refroidissement (température initiale et alpha) pour surpasser systématiquement le HC sur des instances de taille moyenne.

---

## 📈 Visualisation et Convergence

### 🔹 Courbes de Convergence
On observe que le Hill Climbing converge très rapidement vers un palier, tandis que le Recuit Simulé accepte des solutions moins bonnes au début pour mieux explorer l'espace.
![Convergence 50 villes]<img width="884" height="744" alt="image" src="https://github.com/user-attachments/assets/0ba5a7c0-a4ed-4973-a86a-6ddceb3a2d48" />


### 🔹 Meilleur Trajet Trouvé (Map)
Visualisation du circuit hamiltonien optimisé sans croisements grâce à l'opérateur 2-opt.
![Best Route](<img width="853" height="733" alt="image" src="https://github.com/user-attachments/assets/033b10fb-3aa5-465c-8909-f4a6cec273d4" />


---

## ⚙️ Installation et Exécution

### 1️⃣ Configuration
```bash
git clone [https://github.com/atiqaessayouti/TSP-Project.git](https://github.com/atiqaessayouti/TSP-Project.git)
cd TSP-Project
pip install numpy matplotlib
