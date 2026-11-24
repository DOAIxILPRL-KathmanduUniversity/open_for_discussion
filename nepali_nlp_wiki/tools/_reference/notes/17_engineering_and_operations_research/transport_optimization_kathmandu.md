# Masterclass: Optimizing Charging Station Locations (Kathmandu Valley)

> [!IMPORTANT] Gist
> This module details the optimization of Electric Vehicle Charging Station (EVCS) placement for public transport routes in Kathmandu Valley, based on Pulchowk Campus Thesis T16/079. It combines spatial clustering, Multi-Criteria Decision Analysis (MCDA), and Genetic Algorithms.

## 1. Spatial Clustering (Candidate Selection)
Instead of searching the entire valley, we identify high-density boarding/alighting zones using **K-Means Clustering**.
- **Elbow Method**: Used to determine the optimal number of clusters ($k$).
- **Centroids**: These serve as the candidate locations for station placement.

## 2. Suitability Analysis (AHP Weights)
Each candidate is scored based on environmental and infrastructure constraints using the **Analytic Hierarchy Process (AHP)**:

| Criterion | Weight |
| :--- | :--- |
| **Land Use (Commercial)** | 0.179 |
| **Proximity to Roads** | 0.125 |
| **Proximity to Power Grid** | 0.081 |
| **Land Use (Public)** | 0.167 |
| **Slope / Topography** | 0.033 |

**Property Acquisition Cost**: Calculated as $Cost = \frac{Land\ Cost}{Suitability\ Score}$. This ensures we prioritize highly suitable land while minimizing expenditure.

## 3. Genetic Algorithm (GA) Optimization
The final selection is a multi-objective optimization problem:
- **Objective**: $\text{Minimize } (\text{Total Cost} - \alpha \times \text{Routes Covered})$
- **Constraint**: A route is covered if $(2 \times \text{Dist to Station} + \text{Daily Length}) \leq \text{Battery Range}$.

---

**Notebook**: [transport_charging_optimizer.py](notebooks/transport_charging_optimizer.py) (GA-based Spatial Optimizer)

#engineering #operations-research #transportation #evcs #kathmandu #optimization
