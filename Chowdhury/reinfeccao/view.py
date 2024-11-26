import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from Cell import Cell
import matplotlib.colors as colors

def printMatrix(population : Cell, day, execution):
    plt.clf()
    # Extract cell states into a NumPy array
    state_grid = np.array([[cell.state for cell in row] for row in population])

    # Configure color mapping
    cmap = colors.ListedColormap(['white', 'blue', 'red', '#90ee90'])
    bounds = [0, 1, 2, 3, 4]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # Create the plot
    plt.imshow(state_grid, cmap=cmap, norm=norm)
    plt.colorbar(ticks=bounds, boundaries=bounds)
    plt.title(f"COVID-19 Simulation - Day {day} - Execution {execution}")
    plt.pause(0.01) 

def printMatrixGraficoDeLinhaMedio(lattices):
    plt.clf()  
    
    # Pré-alocação das listas
    num_days = len(lattices[0])
    sucetiveis = [0] * num_days
    expostos = [0] * num_days
    infectados = [0] * num_days
    recuperados = [0] * num_days

    sucetiveisMedio = [0] * num_days
    expostosMedio = [0] * num_days
    infectadosMedio = [0] * num_days
    recuperadosMedio = [0] * num_days

    for lattice_index in range(len(lattices)):
        for day, lattice in enumerate(lattices[lattice_index]):
        # rest of your code
            # Uso de compreensões de lista para contar estados
            countSucetiveis = sum(1 for row in lattice for cell in row if cell.state == 0)
            countExpostos = sum(1 for row in lattice for cell in row if cell.state == 1)
            countInfectados = sum(1 for row in lattice for cell in row if cell.state == 2)
            countRecuperados = sum(1 for row in lattice for cell in row if cell.state == 3)
            
            # Atualização das listas pré-alocadas
            sucetiveis[day] += countSucetiveis
            expostos[day] += countExpostos
            infectados[day] += countInfectados
            recuperados[day] += countRecuperados

    for day in range(num_days):
        sucetiveisMedio[day] = sucetiveis[day] / len(lattices)
        expostosMedio[day] = expostos[day] / len(lattices)
        infectadosMedio[day] = infectados[day] / len(lattices)
        recuperadosMedio[day] = recuperados[day] / len(lattices)


    # Plotagem dos gráficos
    
    plt.plot(infectadosMedio, label='I(t)', color='orange')

    
    plt.legend()
    plt.title("COVID-19 Simulation")
    plt.xlabel("time in days")
    plt.ylabel("E(t), I(t)")
    plt.draw()
    plt.show()