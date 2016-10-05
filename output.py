__author__ = 'B2046470858'
import parameters
from numpy import mean
import statistics
import os

def save_general_agents_data(my_agents, decision):
    # check if there is the file as the same name, if is TRUE delete the file
    if os.path.isfile(os.path.join(parameters.OUTPUT_PATH, "temp_general_agents_pop_%s_decision_%s_time_%s.txt" %
            (parameters.pop_redutor, decision, parameters.final_Time))) is True and statistics.my_stats.time == 0:
        os.remove(os.path.join(parameters.OUTPUT_PATH, "temp_general_agents_pop_%s_decision_%s_time_%s.txt" %
                               (parameters.pop_redutor, decision, parameters.final_Time)))
    agents_txt = open(os.path.join(parameters.OUTPUT_PATH, "temp_general_agents_pop_%s_decision_%s_time_%s.txt" %
                                   (parameters.pop_redutor, decision, parameters.final_Time)), 'a')
    for index in range(len(parameters.my_n.get_cod())):
        agents_txt.write('%s, %s, %.2f, %.2f \n' % (statistics.my_stats.time, parameters.my_n.get_cod()[index],
                                                  mean([agent.get_utility() for agent in my_agents if agent.get_mun() == parameters.my_n.get_cod()[index]]),
        mean([agent.get_effort() for agent in my_agents if agent.get_mun() == parameters.my_n.get_cod()[index]])))

    agents_txt.close()


def save_general_firms_data(my_stats, max_size, total_effort, mean_agent_effort, decision):
    # check if there is the file as the same name, if is TRUE delete the file
    if os.path.isfile(os.path.join(parameters.OUTPUT_PATH,"temp_general_firms_pop_%s_decision_%s_time_%s.txt" %
            (parameters.pop_redutor, decision, parameters.final_Time))) is True and statistics.my_stats.time == 0:
        os.remove(os.path.join(parameters.OUTPUT_PATH,"temp_general_firms_pop_%s_decision_%s_time_%s.txt" %
                               (parameters.pop_redutor, decision, parameters.final_Time)))
    firms_txt = open(os.path.join(parameters.OUTPUT_PATH,"temp_general_firms_pop_%s_decision_%s_time_%s.txt" %
                                  (parameters.pop_redutor, decision, parameters.final_Time)), 'a')
    firms_txt.write('%s, %s, %.2f, %.2f, %.2f, %.2f, %.2f , %.2f, %.2f, %.2f \n' % (my_stats.get_time(),
                                                                             my_stats.get_total_firms(),
                                                                             my_stats.get_average_output(),
                                                                             my_stats.get_average_age(),
                                                                             my_stats.get_average_size(),
                                                                             my_stats.get_new_firms(),
                                                                             my_stats.get_exit_firms(),
                                                                             max_size,
                                                                             total_effort,
                                                                             mean_agent_effort))
    firms_txt.close()


def save_firms_data(my_firms, decision, my_stats):
    # check if there is the file as the same name, if is TRUE delete the file
    if os.path.isfile(os.path.join(parameters.OUTPUT_PATH,"temp_firms_pop_%s_decision_%s_time_%s.txt" %
            (parameters.pop_redutor, decision, parameters.final_Time))) is True and statistics.my_stats.time == 0:
        os.remove(os.path.join(parameters.OUTPUT_PATH,"temp_firms_pop_%s_decision_%s_time_%s.txt" %
                               (parameters.pop_redutor, decision, parameters.final_Time)))
    firm_txt = open(os.path.join(parameters.OUTPUT_PATH,"temp_firms_pop_%s_decision_%s_time_%s.txt" %
                                 (parameters.pop_redutor, decision, parameters.final_Time)), 'a')
    for firm in my_firms:
        firm_txt.write('%s, %s, %s, %s, %s, %s, %2f \n' % (statistics.my_stats.time,
                                                      firm.unique_number,
                                                      firm.first_year,
                                                      firm.last_year,
                                                      firm.get_age(statistics.my_stats.time),
                                                      len(firm.members),
                                                      firm.output))
    firm_txt.close()