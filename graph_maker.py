import csv
from NN import NearestNeighbor
from ACO import AntColonyOptimization
from math import radians, sin, cos, sqrt, atan2

# Load city data from CSV file
def load_city_data(filename):
    cities = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            cities[row[0]] = (float(row[1]), float(row[2]))
    return cities

# Haversine distance calculation
def haversine(coord1, coord2):
    # Radius of the Earth in kilometers
    R = 6371.0

    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


# Nearest Neighbor Algorithm
def run_nearest_neighbor(distances, num_cities):
    nn = NearestNeighbor(distances)
    return nn.tsp_nearest_neighbor()

# Ant Colony Optimization Algorithm
def run_ant_colony_optimization(distances, num_cities):
    aco = AntColonyOptimization(distances, num_ants=10, num_iterations=50)
    return aco.run()

# Write results to CSV
def write_results_to_csv(results):
    with open('graph.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['algo_name', 'total_cities', 'optimal_distance'])
        for result in results:
            writer.writerow(result)

if __name__ == "__main__":
    cities = load_city_data('city_data.csv')
    algorithms = {
        'NearestNeighbor': run_nearest_neighbor,
        'AntColonyOptimization': run_ant_colony_optimization
    }

    results = []

    # Iterate over the number of cities
    for num_cities in range(4, 500):
        print(num_cities)
        for algo_name, algo_func in algorithms.items():
            selected_cities = list(cities.keys())[:num_cities]
            distances = [[haversine(cities[city1], cities[city2]) for city2 in selected_cities] for city1 in selected_cities]
            path, distance = algo_func(distances, num_cities)
            results.append([algo_name, num_cities, distance])

    write_results_to_csv(results)
    print("Results written to graph.csv")