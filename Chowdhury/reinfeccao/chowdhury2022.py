import view
from Rules import Rules
import copy

def main():
    latency_period = 8
    infection_period = 10
    exponent = 1.3449
    lattice_size = 51
    days = 250
    disease_transmission_probability = 0.2406

    latticesMedios = []

    for execution in range(0, 1):

        rule = Rules(latency_period, infection_period, exponent, lattice_size, days, disease_transmission_probability)
        lattice = rule.create_new_matrix_with_infected_in_middle()

        lattices = []

        for day in range(1, rule.days + 1):
            view.printMatrix(lattice, day, execution)
            lattices.append(copy.deepcopy(lattice))
            rule.apply_rules(lattice, day)
            rule.update_matrix_with_next_iteration(lattice)
        latticesMedios.append(lattices)

    print("Fim da simulação")
    view.printMatrixGraficoDeLinhaMedio(latticesMedios)