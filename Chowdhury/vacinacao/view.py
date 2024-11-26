import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from Cell import Cell
import matplotlib.colors as colors

def printMatrix(population : Cell, day):
    plt.clf()
    # Extract cell states into a NumPy array
    state_grid = np.array([[cell.state for cell in row] for row in population])

    # Configure color mapping
    cmap = colors.ListedColormap(['white', 'blue', 'red', '#90ee90', 'green'])
    bounds = [0, 1, 2, 3, 4, 5]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # Create the plot
    plt.imshow(state_grid, cmap=cmap, norm=norm)
    plt.colorbar(ticks=bounds, boundaries=bounds)
    plt.title(f"COVID-19 Simulation - Day {day}")
    plt.pause(0.01) 

def printMatrixGraficoDeLinha(lattices):
    plt.clf()  
    
    # Pré-alocação das listas
    num_days = len(lattices)
    sucetiveis = [0] * num_days
    expostos = [0] * num_days
    infectados = [0] * num_days
    recuperados = [0] * num_days
    vacinados = [0] * num_days

    for day, lattice in enumerate(lattices):
        # Uso de compreensões de lista para contar estados
        countSucetiveis = sum(1 for row in lattice for cell in row if cell.state == 0)
        countExpostos = sum(1 for row in lattice for cell in row if cell.state == 1)
        countInfectados = sum(1 for row in lattice for cell in row if cell.state == 2)
        countRecuperados = sum(1 for row in lattice for cell in row if cell.state == 3)
        countVacinados = sum(1 for row in lattice for cell in row if cell.state == 4)
        
        # Atualização das listas pré-alocadas
        sucetiveis[day] = countSucetiveis
        expostos[day] = countExpostos
        infectados[day] = countInfectados
        recuperados[day] = countRecuperados
        vacinados[day] = countVacinados
    
    # Plotagem dos gráficos
    
    plt.plot(infectados, label='Infectados', color='red')
    plt.plot(expostos, label='Expostos', color='orange')
    plt.plot(sucetiveis, label='Sucetíveis', color='blue')
    plt.plot(recuperados, label='Recuperados', color='brown')
    
    plt.legend()
    plt.title("COVID-19 Simulation")
    plt.xlabel("Days")
    plt.ylabel("Number of cells")
    plt.draw()
    plt.show()