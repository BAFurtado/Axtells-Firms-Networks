import random
from pandas import read_csv
import os

# running time of the model
final_Time = 50
time_to_cut_plots = 2
pop_redutor = 0.0015

# number of agents in the simulation
pop_table = read_csv("pop.csv", sep=";", header=0, decimal=',')

# defining the path to save the output
OUTPUT_PATH = '//storage4/carga/modelo dinamico de simulacao/exits_python/'

# checking the presence of output and creating the folder if there isn't
if os.path.exists(os.path.join(OUTPUT_PATH, 'Results')) is False:
    os.mkdir(os.path.join(OUTPUT_PATH, 'Results'))

# formatting the output path
OUTPUT_PATH = os.path.join(OUTPUT_PATH, 'Results')

cod = []
pop_mun = []
for item in range(len(pop_table['cod_mun'])):
    cod.append(int(pop_table['cod_mun'][item]))
    pop_mun.append(int(pop_table['2010'][item] * pop_redutor))

pop = sum(pop_mun)

if time_to_cut_plots >= final_Time:
    vars()['time_to_cut_plots'] = int(final_Time/2)-1

class N:
    def __init__(self, pop, cod, pop_mun):
        self.total_n = pop
        self.old = self.total_n
        self.cod = cod
        self.pop_mun = pop_mun

    def get_n(self):
        return self.total_n

    def set_n(self, n):
        self.total_n = n

    def set_old(self):
        self.old = self.total_n

    def get_old(self):
        return self.old

    def get_cod(self):
        return self.cod

    def get_pop_mun(self):
        return self.pop_mun

    def update_n(self):
        self.total_n += 1

    def __str__(self):
        return str(self.total_n)

my_n = N(pop, cod, pop_mun)

# endowments
omega = 1

# agent activations per period
activation = int(my_n.get_n() * .04)



# time calibration: one model period one month of calendar time
# initial condition all agents in singleton firms
