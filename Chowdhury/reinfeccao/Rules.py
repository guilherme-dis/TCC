import math
import numpy as np
import random as random
from Cell import Cell
import chowdhury2022

class Rules:
    def __init__(self, latency_period, infection_period, exponent, lattice_size, days, disease_transmission_probability):
        self.latency_period = latency_period
        self.infection_period = infection_period
        self.exponent = exponent
        self.lattice_size = lattice_size
        self.days = days
        self.disease_transmission_probability = disease_transmission_probability
        self.Pint = self.calcule_Pint()

    def update_matrix_with_next_iteration(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                new_state = matrix[i][j].get_state_in_next_iteration()
                matrix[i][j].set_date_last_updated(matrix[i][j].get_date_last_updated() + 1) 
                if new_state != matrix[i][j].get_state():
                    matrix[i][j].set_state(new_state)
                    matrix[i][j].set_date_last_updated(0)

    def create_new_matrix_with_infected_in_middle(self):
        matrix = [[Cell(0) for _ in range(self.lattice_size)] for _ in range(self.lattice_size)]
        line =  int(((self.lattice_size - 1) / 2))
        column = int(((self.lattice_size - 1) / 2))
        matrix[line][column].set_state(2)
        matrix[line][column].set_state_in_next_iteration(2)
        return np.array(matrix)

    def calculate_reinfection_probability(days_recovered):
        if days_recovered < 60:
            return 0.2
        elif days_recovered < 90:
            return 0.3
        elif days_recovered < 120:
            return 0.4
        elif days_recovered < 150:
            return 0.5
        else:
            return 0.1

    def getProbabilityOfInfection(self, position, matrix, reinfection_probability):
        x, y = position
        raio = int((self.lattice_size - 1) / 2)
 
        PIAll = []

        for l in range(1, raio + 1):
            number_of_infected = 0
            number_of_cells = l * 8

            minimoX = x - l
            minimoY = y - l
            maximoX = x + l
            maximoY = y + l


            # Calculate the number of infected cells in the layer
            for i in range(minimoX, maximoX + 1):
                if i in (minimoX, maximoX):
                    for j in range(minimoY, maximoY + 1):
                        icount = i
                        jcount = j

                        
                        if i<0:
                            icount = self.lattice_size + i
                        if j<0:
                            jcount = self.lattice_size + j
                        if i>=self.lattice_size:
                            icount = i - self.lattice_size
                        if j>=self.lattice_size:
                            jcount = j - self.lattice_size

                        if matrix[icount][jcount].get_state() == 2:
                            number_of_infected += 1
                else:
                    icount = i
                    minimoYcount = minimoY
                    maximoYcount = maximoY

                    if i<0:
                        icount = self.lattice_size + i
                    if i>=self.lattice_size:
                        icount = i - self.lattice_size
                    
                    if minimoY < 0:
                        minimoYcount = self.lattice_size + minimoY
                    
                    if maximoY >= self.lattice_size:
                        maximoYcount = maximoY - self.lattice_size

                    if matrix[icount][minimoYcount].get_state() == 2:
                        
                        number_of_infected += 1
                    if matrix[icount][maximoYcount].get_state() == 2:
                        number_of_infected += 1
                        
            PI = number_of_infected / number_of_cells
            PIAll.append(PI)

        # Calculate the probability of infection in the cell
        Presult = []

        Presult = [PIAll[i] * self.Pint[i] for i in range(len(PIAll))]

        return math.fsum(Presult) * self.disease_transmission_probability * reinfection_probability

    def apply_rules(self, matrix, day):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):

                if matrix[i][j].get_state() == 0:
                    probabilidade = self.getProbabilityOfInfection((i, j), matrix, 1)

                    if (probabilidade>random.random()):
                        print(probabilidade)
                        print("INFECTORU")
                        matrix[i][j].set_state_in_next_iteration(1)

                elif matrix[i][j].get_state() == 1:
                    if matrix[i][j].get_date_last_updated() >= self.latency_period:
                        matrix[i][j].set_state_in_next_iteration(2)

                elif matrix[i][j].get_state() == 2:
                    if matrix[i][j].get_date_last_updated() >= self.infection_period:
                        matrix[i][j].set_state_in_next_iteration(3)

                elif matrix[i][j].get_state() == 3:

                    #reinfection_probability = self.calculate_reinfection_probability(matrix[i][j].get_days_recovered())

                    if matrix[i][j].get_days_recovered() < 60:
                        reinfection_probability = 0.2
                    elif matrix[i][j].get_days_recovered() < 90:
                        reinfection_probability = 0.3
                    elif matrix[i][j].get_days_recovered() < 120:
                        reinfection_probability = 0.4
                    elif matrix[i][j].get_days_recovered() < 150:
                        reinfection_probability = 0.5
                    else:
                        reinfection_probability = 0.1
                    
                    probabilidade = self.getProbabilityOfInfection((i, j), matrix, reinfection_probability)

                    if (probabilidade>random.random()):
                        print(probabilidade)
                        print("RE_INFECTOU")
                        matrix[i][j].set_state_in_next_iteration(1)
                    else:
                        matrix[i][j].increment_days_recovered()
                    

    def calcule_Pint(self):#Equação 5
        raio = int((self.lattice_size - 1) / 2)
        n = self.exponent
        An = 0

        for l in range(1, raio+1):
            An += (1 /  (l ** n))

        Pint = []
        for l in range(1, raio+1) :
            Pint.append(1 / (An * (l ** n)))
        return Pint


def main():
    chowdhury2022.main()


if __name__ == "__main__":
   main()
