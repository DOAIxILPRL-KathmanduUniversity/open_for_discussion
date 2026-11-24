import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
# Note: Ensure 'geneticalgorithm' is installed: !pip install geneticalgorithm
from geneticalgorithm import geneticalgorithm as ga

# --- 0. DATA SIMULATION ---
def simulate_data(num_stops=1000, num_routes=130):
    print("--- Step 0: Simulating Data ---")
    stops = np.random.randn(num_stops, 2) * [2, 3] + [10, 10]
    stops = np.vstack([stops, np.random.rand(num_stops // 4, 2) * [20, 30]])
    routes = []
    for i in range(num_routes):
        start = np.random.rand(2) * [15, 25] + [2, 2]
        end = np.random.rand(2) * [15, 25] + [2, 2]
        daily_length = np.random.uniform(50, 220)
        routes.append({
            "route_id": f"R{i+1}",
            "start_x": start[0], "start_y": start[1],
            "end_x": end[0], "end_y": end[1],
            "daily_length_km": daily_length
        })
    return pd.DataFrame(stops, columns=['x', 'y']), pd.DataFrame(routes)

# --- 1. CLUSTERING ---
def find_optimal_k(points, max_k=30):
    inertias = []
    K = range(1, max_k + 1)
    for k in K:
        kmeanModel = KMeans(n_clusters=k, n_init='auto', random_state=42)
        kmeanModel.fit(points)
        inertias.append(kmeanModel.inertia_)
    diffs = np.diff(inertias, 2)
    elbow_k = np.argmax(diffs) + 2
    return elbow_k

def run_kmeans(points, k):
    kmeans = KMeans(n_clusters=k, n_init='auto', random_state=42)
    kmeans.fit(points)
    centroids = kmeans.cluster_centers_
    candidate_locations = pd.DataFrame(centroids, columns=['x', 'y'])
    candidate_locations['cluster_id'] = range(k)
    return candidate_locations

# --- 2. SUITABILITY ANALYSIS (AHP) ---
def calculate_suitability_score(locations):
    ahp_weights = {
        'proximity_river': 0.014, 'proximity_vegetation': 0.033, 'slope': 0.033,
        'proximity_petrol': 0.028, 'proximity_power': 0.081, 'proximity_roads': 0.125,
        'proximity_evcs': 0.126, 'land_use_public': 0.167, 'land_use_commercial': 0.179,
        'land_use_residential': 0.110, 'land_use_industrial': 0.057, 'land_use_agricultural': 0.047
    }
    np.random.seed(42)
    locations['dist_river_m'] = np.random.uniform(50, 1000, len(locations))
    locations['dist_road_m'] = np.random.uniform(10, 800, len(locations))
    locations['slope_percent'] = np.random.uniform(1, 30, len(locations))
    locations['land_use'] = np.random.choice(['Commercial', 'Residential', 'Public', 'Agricultural', 'Industrial'], len(locations))
    locations['land_cost_per_sqm'] = locations['land_use'].map({
        'Commercial': 150000, 'Public': 120000, 'Residential': 80000,
        'Industrial': 40000, 'Agricultural': 30000
    }) + np.random.uniform(-5000, 5000, len(locations))

    def normalize(value, thresholds, ascending=True):
        scores = [1.0, 0.75, 0.5, 0.25]
        if not ascending: scores = scores[::-1]
        for i, threshold in enumerate(thresholds):
            if value < threshold: return scores[i]
        return scores[-1]

    scores = []
    for _, loc in locations.iterrows():
        score_river = normalize(loc['dist_river_m'], [125, 250, 500], ascending=False)
        score_slope = normalize(loc['slope_percent'], [7, 12, 25], ascending=True)
        score_road = normalize(loc['dist_road_m'], [125, 250, 500], ascending=True)
        score_land_use = ahp_weights.get(f"land_use_{loc['land_use'].lower()}", 0)
        final_score = (score_river * 0.014 + score_slope * 0.033 + score_road * 0.125 + score_land_use)
        scores.append(final_score)

    locations['suitability_score'] = scores
    locations['property_cost'] = locations['land_cost_per_sqm'] / locations['suitability_score']
    return locations

# --- 3. OPTIMIZATION ---
def run_optimization(candidate_locations, routes, battery_range):
    terminals_coords = np.vstack([routes[['start_x', 'start_y']].values, routes[['end_x', 'end_y']].values])
    candidate_coords = candidate_locations[['x', 'y']].values
    dist_matrix = cdist(terminals_coords, candidate_coords)

    def optimization_objective(individual):
        selected_indices = np.where(np.array(individual) == 1)[0]
        if len(selected_indices) == 0: return 1e12
        total_property_cost = candidate_locations.iloc[selected_indices]['property_cost'].sum()
        covered_routes = 0
        for i, route in routes.iterrows():
            start_dists = dist_matrix[i, selected_indices]
            end_dists = dist_matrix[i + len(routes), selected_indices]
            if (2 * min(np.min(start_dists), np.min(end_dists)) + route['daily_length_km']) <= battery_range:
                covered_routes += 1
        return total_property_cost - (50000 * covered_routes)

    model = ga(function=optimization_objective, dimension=len(candidate_locations),
               variable_type='bool', algorithm_parameters={'max_num_iteration': 50, 'population_size': 30})
    model.run()
    return candidate_locations.iloc[np.where(np.array(model.best_variable) == 1)[0]]

if __name__ == "__main__":
    bus_stops, transport_routes = simulate_data()
    optimal_k = find_optimal_k(bus_stops[['x', 'y']].values)
    candidates = run_kmeans(bus_stops[['x', 'y']].values, k=optimal_k)
    candidates = calculate_suitability_score(candidates)
    stations = run_optimization(candidates, transport_routes, battery_range=100)
    print(f"Optimal Stations Identified: {len(stations)}")
