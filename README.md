# Dinâmica endógena de firmas formadas por agentes em rede: uma análise exploratória
# Endogenous dynamics of firms made up by networked agents: an exploratory analysis

This is an adaptation of Axtell (2013) model of endogenous firms. This model applies Axtell's model including one change 
in the network.

## How to cite?

This working paper has been published.
Please, cite as: FURTADO, Bernardo Alves; MESSA, Alexandre Silva; EBERHARDT, Isaque Daniel Rocha and MACIENTE, Aguinaldo 
N. **Endogenous dynamics of firms made up by networked agents: an exploratory analysis** RADAR, n. 45, p. 19-32, IPEA: Brasília, 2016. 

Available here https://www.researchgate.net/publication/304659905_Dinamica_endogena_de_firmas_formadas_por_agentes_em_rede_uma_analise_exploratoria

## Who to talk to?

bernardo.furtado@ipea.gov.br

## Setting up the simulation

In order to run the model you have to set at the parameters.py
1. OUTPUT_PATH which is a directory where the program will save data and figures
2. Determine at parameters.py the length of the model (*final_time*) and the *adjustment time*. We suggest 600 and 200.
3. Define the percentage of population to run. We run using data for Brasília and its neighboring municipalities and run
with a 0.05% percentage. You can replace pop.csv with your own set of municipalities and their population numbers.

## Running it

You have two options to run the model. A single run - in which the network is complete - so that all agents can connect
with all other agents. 

Or you can restrict the network to only those agents that are located at the same municipality.

To run the single model, alter **controller** to False in *parameters* and simply run:

**python main.py**

To run the model twice, once for the full the network *True* and once for the restricted network *False*, 
alter **controller** to True in *parameters* and simply run:
 
**python control.py**
