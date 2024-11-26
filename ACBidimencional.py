import view as view  # Importa os graficos
import numpy as np
import matplotlib.pyplot as plt

def getNewPoint(MALHA, line, column):
    # contar vizinhos
    vizinhos = 0

    for i in range(line - 1, line + 2):
        for j in range(column - 1, column + 2):
            if i == line and j == column:
                continue
            try:
                vizinhos += MALHA[i][j]
            except:
                pass



    if vizinhos <= 1:
        return 0
    if (vizinhos == 2 or vizinhos == 3) and MALHA[line][column] == 1:
        return 1
    if vizinhos == 3:
        return 1
    return 0

def decimal_to_binary(decimal_value):
    if 0 <= decimal_value < 256:
        binary_representation = format(decimal_value, '08b')
        return binary_representation
    else:
        raise ValueError("O valor decimal deve estar entre 0 e 255.")


def applyRules(MALHA):
    NEW_MALHA = np.zeros(MALHA.shape, dtype=int)
    for i in range(0, MALHA.shape[0]):
        for j in range(0, MALHA.shape[1]):
            NEW_MALHA[i][j] = getNewPoint(MALHA, i, j)
    return NEW_MALHA


def game_of_life():
    LINES = 50
    COLUMNS = 50

    MALHA = np.zeros((LINES, COLUMNS), dtype=int)

    middleLine = int(LINES / 2)
    middleColumn = int(COLUMNS / 2)

    # gerar um glider no centro da malha
    MALHA[middleLine][middleColumn] = 1
    MALHA[middleLine + 1][middleColumn + 1] = 1
    MALHA[middleLine + 2][middleColumn + 1] = 1
    MALHA[middleLine + 2][middleColumn] = 1
    MALHA[middleLine + 2][middleColumn - 1] = 1

    # gerar um blinker no canto da malha
    MALHA[1][1] = 1
    MALHA[1][2] = 1
    MALHA[1][3] = 1

    # gerar um blinker no canto da malha
    MALHA[4][4] = 1
    MALHA[4][5] = 1
    MALHA[4][6] = 1
    MALHA[5][4] = 1
    MALHA[5][5] = 1
    MALHA[5][6] = 1
    MALHA[6][4] = 1
    MALHA[6][5] = 1
    MALHA[6][6] = 1
    



    for i in range(0, 100):
        plot_binary_vectors(MALHA)
        MALHA = applyRules(MALHA)
        
def plot_binary_vectors(malha):
    plt.imshow(malha, cmap='binary', interpolation='nearest')
    plt.pause(0.1)  # Adicionar um atraso de 0.1 segundos
    plt.clf() 

def main():
    game_of_life()


if __name__ == "__main__":
    main()
