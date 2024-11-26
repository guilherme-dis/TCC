import view as view  # Importa os graficos
import numpy as np

def getRule(rule, left, center, rigth):
    if left == 1 and center == 1 and rigth == 1:
        return rule[0]
    elif left == 1 and center == 1 and rigth == 0:
        return rule[1]
    elif left == 1 and center == 0 and rigth == 1:
        return rule[2]
    elif left == 1 and center == 0 and rigth == 0:
        return rule[3]
    elif left == 0 and center == 1 and rigth == 1:
        return rule[4]
    elif left == 0 and center == 1 and rigth == 0:
        return rule[5]
    elif left == 0 and center == 0 and rigth == 1:
        return rule[6]
    elif left == 0 and center == 0 and rigth == 0:
        return rule[7]


def generate_population(rule):
    MAX_ITERATIONS_LINES = 10
    MAX_ITERATIONS_COLUMNS = 20

    population = np.zeros((MAX_ITERATIONS_LINES, MAX_ITERATIONS_COLUMNS), dtype=int)
    middle = int(MAX_ITERATIONS_COLUMNS / 2)
    population[0][middle] = 1

    for i in range(1, MAX_ITERATIONS_LINES):
        for j in range(0, MAX_ITERATIONS_COLUMNS):
            if j == 0:
                population[i][j] = getRule(
                    rule,
                    population[i - 1][MAX_ITERATIONS_COLUMNS-1],
                    population[i - 1][j],
                    population[i - 1][j + 1]
                )

            elif j == MAX_ITERATIONS_COLUMNS - 1:
                population[i][j] = getRule(
                    rule,
                    population[i - 1][j - 1],
                    population[i - 1][j],
                    population[i - 1][0]
                )

            else:
                population[i][j] = getRule(
                    rule,
                    population[i - 1][j - 1],
                    population[i - 1][j],
                    population[i - 1][j + 1],
                )
    #limpa o grafico se já estiver e cria um novo

    #plota o grafico
    view.plot_binary_vector(population)

def decimal_to_binary(decimal_value):
    if 0 <= decimal_value < 256:
        binary_representation = format(decimal_value, '08b')
        return binary_representation
    else:
        raise ValueError("O valor decimal deve estar entre 0 e 255.")
    
def main():
    generate_population(util.decimal_to_binary(62))
    print(decimal_to_binary(62))





if __name__ == "__main__":
    main()
