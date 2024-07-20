import pandas as pd
import matplotlib.pyplot as plt

# Read data from graph.csv
data = pd.read_csv('graph.csv')

# Separate data for each algorithm
bnb_data = data[data['algo_name'] == 'BranchAndBound']
nn_data = data[data['algo_name'] == 'NearestNeighbor']
aco_data = data[data['algo_name'] == 'AntColonyOptimization']

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the data with different styles
ax.plot(bnb_data['total_cities'], bnb_data['optimal_distance'], marker='o', label='Branch and Bound', linestyle='-')
ax.plot(nn_data['total_cities'], nn_data['optimal_distance'], marker='s', label='Nearest Neighbor', linestyle='--')
ax.plot(aco_data['total_cities'], aco_data['optimal_distance'], marker='^', label='Ant Colony Optimization', linestyle='-.')

# Customizing the appearance
ax.set_title('Optimal Distance vs. Number of Cities', fontsize=18)
ax.set_xlabel('Number of Cities', fontsize=14)
ax.set_ylabel('Optimal Distance (km)', fontsize=14)
ax.legend(fontsize=12)
ax.grid(True)
ax.tick_params(axis='both', which='major', labelsize=12)

# Add background color
ax.set_facecolor('#FFC94A')

# Tight layout
plt.tight_layout()

# Save or show the plot
plt.savefig('optimal_distance_graph.png', dpi=300)
plt.show()
