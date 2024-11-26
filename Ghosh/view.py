import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from GhoshCell import Cell
import matplotlib.colors as colors

def printMatrix(population, day):
    plt.clf()
    # Define mapping from letters to integers
    letter_to_int = {'Blank': 0, 'S': 1, 'E': 2, 'I': 3, 'Q': 4, 'R': 5, '': 6}

    # Extract cell states into a NumPy array of corresponding integers
    state_grid = np.array([[letter_to_int[cell.state] for cell in row] for row in population])

    # Configure color mapping
    cmap = colors.ListedColormap(['black', 'blue', 'green', 'red','cyan', 'yellow'])
    bounds = list(range(len(letter_to_int)))  # assuming continuous integer values starting from 0
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # Create the plot
    plt.imshow(state_grid, cmap=cmap, norm=norm)
    plt.colorbar().set_ticklabels(list(letter_to_int.keys()))
    plt.title(f"COVID-19 Simulation - Day {day}")
    plt.pause(0.5)