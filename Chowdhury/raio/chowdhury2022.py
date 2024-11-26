import view
from Rules import Rules
import copy

def main():
    latency_period = 8
    infection_period = 18
    exponent = 2
    lattice_size = 51
    days = 300
    disease_transmission_probability = 0.3

    rule = Rules(latency_period, infection_period, exponent, lattice_size, days, disease_transmission_probability)
    lattice = rule.create_new_matrix_with_infected_in_middle()

    lattices = []


    for day in range(1, rule.days + 1):
        view.printMatrix(lattice, day)
        lattices.append(copy.deepcopy(lattice))
        rule.apply_rules(lattice)
        rule.update_matrix_with_next_iteration(lattice)
        

    print("Fim da simulação")
    view.printMatrixGraficoDeLinha(lattices)