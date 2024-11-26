from GhoshCell import Cell
import numpy as np
import random
import view


def create_latice(N, density, Iint, Eint):
        
        lattice = [[Cell('Blank') for i in range(N)] for j in range(N)]
        sucetible_cells = random.sample(range(N*N), int(density*N*N))
        for cell in sucetible_cells:
            lattice[cell//N][cell%N].set_state('S')
            lattice[cell//N][cell%N].set_state_in_next_iteration('S')
        
        exposed_cells = random.sample(sucetible_cells, Eint)
        for cell in exposed_cells:
            lattice[cell//N][cell%N].set_state('E')
            lattice[cell//N][cell%N].set_state_in_next_iteration('E')
            sucetible_cells.remove(cell)
        
        #change the state of sucetilbe cells to infected
        infected_cells = random.sample(sucetible_cells, Iint)
        for cell in infected_cells:
            lattice[cell//N][cell%N].set_state('I')
            lattice[cell//N][cell%N].set_state_in_next_iteration('I')
            sucetible_cells.remove(cell)
        return np.array(lattice)

def apply_rules(lattice):
    pe = 0.5
    pi = 0.5
    pq = 0.1
    pr = 0.12
    ti = 8
    tq = 2
    tr = 18
    d = 1

    for i in range(len(lattice)):
        for j in range(len(lattice[i])):
            if lattice[i][j].get_state() == 'S':
                # Rule 1: Getting exposed
                neighbours = get_neighbours(lattice, i, j, d)
                count = count_exposed_infected_neighbours(neighbours,d)
                probability_of_exposure = pe * count

                if random.random() < probability_of_exposure:
                    lattice[i][j].set_state_in_next_iteration('E')

            elif lattice[i][j].get_state() == 'E':
                # Rule 2: Getting infected with symptoms
                if lattice[i][j].get_date_last_updated() >= ti:
                    lattice[i][j].set_state_in_next_iteration('I')
                elif random.random() < pi:
                    lattice[i][j].set_state_in_next_iteration('I')

            elif lattice[i][j].get_state() == 'I':
                # Rule 3: Getting quarantined
                if lattice[i][j].get_date_last_updated() >= tq:
                    lattice[i][j].set_state_in_next_iteration('Q')
                elif random.random() < pq:
                    lattice[i][j].set_state_in_next_iteration('Q')

            elif lattice[i][j].get_state() == 'Q':
                # Rule 4: Recovery or removal
                if lattice[i][j].get_date_last_updated() >= tr:
                    lattice[i][j].set_state_in_next_iteration('R')
                elif random.random() < pr:
                    lattice[i][j].set_state_in_next_iteration('R')

def get_neighbours(lattice, i, j, d):
    neighbours = []
    for x in range(i-d, i+d+1):
        for y in range(j-d, j+d+1):
            if x >= 0 and x < len(lattice) and y >= 0 and y < len(lattice[x]):
                if x != i or y != j:
                    if lattice[x][y].get_state() != 'Blank':
                        neighbours.append(lattice[x][y])
    return neighbours

def count_exposed_infected_neighbours(neighbours):
    count = 0
    for neighbour in neighbours:
        if neighbour.get_state() == 'E' or neighbour.get_state() == 'I':
            count += 1
    
    return count

def update_matrix_with_next_iteration(lattice):
    for i in range(len(lattice)):
        for j in range(len(lattice[i])):
            if lattice[i][j].get_state() == 0:
                continue
            new_state = lattice[i][j].get_state_in_next_iteration()
            lattice[i][j].set_date_last_updated(lattice[i][j].get_date_last_updated() + 1) 
            if new_state != lattice[i][j].get_state():
                lattice[i][j].set_state(new_state)
                lattice[i][j].set_date_last_updated(0)

def main():
    lattice_size = 100
    Infectados_iniciais = 6
    Expostos_iniciais = 200
    days = 100
    density = 0.625
    
    lattice = create_latice(lattice_size, density, Infectados_iniciais, Expostos_iniciais)

    for day in range(1, days):
        view.printMatrix(lattice, day)
        apply_rules(lattice)
        update_matrix_with_next_iteration(lattice)


if __name__ == "__main__":
    main()
