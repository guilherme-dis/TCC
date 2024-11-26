import view
from Rules import Rules
import copy

def main():
    latency_period = 8
    infection_period = 18
    exponent = 3
    lattice_size = 51
    days = 300
    disease_transmission_probability = 0.3
    latticesMedios = []


    

    

    for execution in range(0, 30):

        rule = Rules(latency_period, infection_period, exponent, lattice_size, days, disease_transmission_probability)
        lattice = rule.create_new_matrix_with_infected_in_middle()

        lattices = []

        for day in range(1, rule.days + 1):
            view.printMatrix(lattice, day, execution)
            lattices.append(copy.deepcopy(lattice))
            rule.apply_rules(lattice)
            rule.update_matrix_with_next_iteration(lattice)
        latticesMedios.append(lattices)

    print("Fim da simulação")
    #view.printMatrixGraficoDeLinha(lattices)
    view.printMatrixGraficoDeLinhaMedio(latticesMedios)